from django.core.management.base import BaseCommand
from products.models import Category, Product
import requests
import json

URL_CATEGORIES = "https://fr.openfoodfacts.org/categories.json"


class Command(BaseCommand):
    help = "allows you to populate the database of product objects"

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

    def url_exist(self, url):
        url_exist = Product.objects.get(url=url)
        if url != url_exist:
            return url

    def get_product(self, url_category, index_product):
        """get openfoodfact data and create a Product object
        Args:
            url_category (str): [description]
            index_product (int): [description]

        Returns:
            [Product]: returns the product with the attributes
        """
        response = requests.get(url_category)
        response_json = json.loads(response.text)
        product = response_json["products"][index_product]
        product_name = product["product_name"]
        try:
            nutriscore_grade = product["nutriscore_grade"]
        except KeyError: # noqa
            nutriscore_grade = "0"
        try:
            image_url = product["image_url"]
        except KeyError: # noqa
            image_url = ""
        pnns_groups_1 = product["pnns_groups_1"]
        try:
            ingredients_text = product["ingredients_text"]
        except KeyError: # noqa
            ingredients_text = "pas d'ingrédients renseignés"
        url = product["url"]
        print(f"url du product: {url}")
        try:
            product = Product.objects.create(product_name=product_name,
                                             nutriscore_grade=nutriscore_grade,
                                             image_url=image_url,
                                             pnns_groups_1=Category.objects.get( # noqa
                                                 pnns_groups_1=pnns_groups_1),
                                             ingredients_text=ingredients_text,
                                             url=url)
        except: # noqa
            product = None
        return product

    def handle(self, *args, **options):
        """[summary]
        """
        for url_category in Command.get_list_url_category(self):
            print(f"url categorie json: {url_category}")
            index_product = 0
            count_of_products = 23
            for product in range(0, count_of_products):
                product = Command.get_product(
                    self, url_category, index_product)
                print(product)
                index_product += 1
