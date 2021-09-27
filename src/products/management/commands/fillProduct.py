from django.core.management.base import BaseCommand, CommandError
from products.models import Category, Product
import requests
import json

URL_CATEGORIES = "https://fr.openfoodfacts.org/categories.json"

class Commande(BaseCommand):
    help = "allows you to populate the database of category and product objects "
    
    def get_category(self, url_category, index_product):
        response = requests.get(url_category)
        response_json = json.loads(response.text)
        category = response_json["products"][index_product]
        category = category["pnns_groups_1"]
        category = Category(pnns_groups_1=category)
        return category

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
        return f"{response_json}.json"
    
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
        nutriscore_grade = product["nutriscore_grade"]
        image_url = product["image_url"]
        pnns_groups_1 = Category(product["pnns_groups_1"])
        ingredients_text = product["ingredients_text"]
        url = product["url"]
        print(url)
        product = Product(product_name=product_name, 
                          nutriscore_grade=nutriscore_grade, 
                          image_url=image_url, 
                          pnns_groups_1=pnns_groups_1, 
                          ingredients_text=ingredients_text, 
                          url=url)
        return product
    
    def fill_category_database():
        """[summary]
        """
        index_category = 0
        for url_category in range(0, 100):
            url_category = Product().get_url_category(index_category)
            print(url_category)
            index_product = 0
            for category in range(0, 20):
                category = Category().get_category(url_category, index_product)
                print(category)
                try:
                    category_exist = Category.objects.get(pnns_groups_1=category)
                except:
                    category_exist = None
                print(f"exist: {category_exist}")
                if category_exist != category.pnns_groups_1:
                    category = Category(pnns_groups_1=category)
                    category.save()
                index_product+=1
            index_category+=1
        
    def fill_product_database():
        """[summary]
        """
        index_category = 0
        for url_category in range(0, 100):
            url_category = Product().get_url_category(index_category)
            print(url_category)
            index_category+=1
            index_product = 0
            for product in range(0, 20):
                product = Product().get_product(url_category, index_product)
                print(product)
                url_exist = Product.objects.filter(url = product.url)
                if product.url != url_exist:
                    product.save()
                index_product+=1
