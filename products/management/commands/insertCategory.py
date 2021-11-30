from django.core.management.base import BaseCommand
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
        count_of_tags_category = 1200
        for tags in range(0, count_of_tags_category):
            url_category = Command.get_url_category(self, index_category)
            list_url_category.append(url_category)
            tags += 1
            index_category += 1
        print(f"list catégory: {list_url_category}")
        return list_url_category

    def get_pnns_groups_1(self, url_category, index_tags):
        response = requests.get(url_category)
        response_json = json.loads(response.text)
        try:
            category = response_json["products"][index_tags]["pnns_groups_1"]
        except: # noqa
            category = "0"
        print(f"pnns_groups_1: {index_tags}: {category}")
        try:
            pnns_groups_1 = Category.objects.create(pnns_groups_1=category)
        except: # noqa
            pnns_groups_1 = f"{category} est déjà enregistré dans la base"
        return pnns_groups_1

    def handle(self, *args, **options):
        """[summary]
        """
        for url_json in Command.get_list_url_category(self):
            print(url_json)
            index_tags = 0
            count_of_products = 23
            for category in range(0, count_of_products):
                category = Command.get_pnns_groups_1(
                    self, url_json, index_tags)
                print(category)
                index_tags += 1
