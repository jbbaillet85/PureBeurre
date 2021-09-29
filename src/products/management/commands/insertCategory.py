from django.core.management.base import BaseCommand, CommandError
from products.models import Category
import requests
import json

URL_CATEGORIES = "https://fr.openfoodfacts.org/categories.json"

class Command(BaseCommand):
    help = "allows you to populate the database of category objects "
    
    def get_url_category(self, index_category):
        """get urls in openfoodfact json format 

        Args:
            index_category (int): [description]

        Returns:
            str: returns the url of the category with the format json 
        """
        response = requests.get(URL_CATEGORIES)
        response_json = json.loads(response.text)
        response_json = response_json["tags"][index_category]["url"]
        url_category = f"{response_json}.json"
        print(f"url_category: {index_category}: {url_category}")
        return url_category
    
    def get_list_url_category(self):
        list_url_category = []
        index_category = 0
        tags = 0
        for tags in range(0, 10):
            url_category = Command.get_url_category(self, index_category)
            list_url_category.append(url_category)
            tags +=1
            index_category +=1
        print(f"list catégory: {list_url_category}")
        return list_url_category
            
    def get_pnns_groups_1(self, url_category, index_tags):
        response = requests.get(url_category)
        response_json = json.loads(response.text)
        category = response_json["products"][index_tags]["pnns_groups_1"]
        print(f"pnns_groups_1: {index_tags}: {category}")
        return category
    
    def get_list_pnns_groups_1(self):
        list_pnns_groups_1 = []
        for url_category in Command.get_list_url_category(self):
            print(f"url category: {url_category}")
            index_tags = 0
            for pnns_groups_1 in range(0,23):
                pnns_groups_1 = Command.get_pnns_groups_1(self, url_category, index_tags)
                print(f"pnns_groups_1: {index_tags}: type {type(pnns_groups_1)}: {pnns_groups_1}")
                list_pnns_groups_1.append(pnns_groups_1)
                index_tags +=1
        print(f"liste des pnns_groups_1: {set(list_pnns_groups_1)}")
        return set(list_pnns_groups_1)

    def handle(self, *args, **options):
        """[summary]
        """
        for pnns_groups_1_name in Command.get_list_pnns_groups_1(self):
            print(pnns_groups_1_name)
            try:
                category_exist = Category.objects.get(pnns_groups_1=pnns_groups_1_name)
            except:
                category_exist = None
            print(f"exist: {category_exist}")
            if category_exist != pnns_groups_1_name:
                category = Category.objects.create(pnns_groups_1=pnns_groups_1_name)
                category.save()
