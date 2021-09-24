from django.db import models
import json
import requests

URL_CATEGORIES = "https://fr.openfoodfacts.org/categories.json"

class Category(models.Model):
    pnns_groups_1 = models.CharField(max_length=150, default="0", unique=True)
    
    def __str__(self) -> str:
        return self.pnns_groups_1
    
    def get_category(self, url_category, index_product):
        response = requests.get(url_category)
        response_json = json.loads(response.text)
        category = response_json["products"][index_product]
        category = category["pnns_groups_1"]
        category = Category(pnns_groups_1=category)
        return category

class Nutriscore(models.Model):
    nutriscore_grade=models.CharField(max_length=1, default="0", unique=True)
    
    def __str__(self) -> str:
        return self.nutriscore_grade

class Product(models.Model):
    product_name= models.CharField(max_length=150, default="pas de nom de produit")
    nutriscore_grade=models.ForeignKey(Nutriscore, on_delete=models.CASCADE, default="")
    image_url=models.ImageField(default="")
    pnns_groups_1=models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    ingredients_text=models.TextField(default="pas d'ingrédients renseignés")
    url=models.URLField(unique=True)
    
    def __str__(self) -> str:
        return self.url

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
        try:
            nutriscore_grade = product["nutriscore_grade"]
        except:
            nutriscore_grade = Nutriscore("0")
        image_url = product["image_url"]
        pnns_groups_1 = product["pnns_groups_1"]
        ingredients_text = product["ingredients_text"]
        url = product["url"]
        print(url)
        nutriscore = Nutriscore(nutriscore_grade=nutriscore_grade)
        category = Category(pnns_groups_1=pnns_groups_1)
        product = Product(product_name=product_name, 
                          nutriscore_grade=nutriscore.nutriscore_grade, 
                          image_url=image_url, 
                          pnns_groups_1=category, 
                          ingredients_text=ingredients_text, 
                          url=url)
        return product

    def fill_nutriscore_database():
        """[summary]
        """
        list_nutriscores = ["a","b","c","d","e"]
        for nutriscore in list_nutriscores:
            nutriscores = Nutriscore.objects.filter(nutriscore_grade = nutriscore)
            if nutriscore != nutriscores[0]:
                nutriscore = Nutriscore(nutriscore_grade=nutriscore)
                nutriscore.save()
    
    def fill_init_category_database():
        init_category = Category(pnns_groups_1="Sugary snacks")
        init_category.save()
    
    def fill_category_database():
        """[summary]
        """
        list_category = []
        index_category = 0
        for url_category in range(0, 100):
            url_category = Product().get_url_category(index_category)
            print(url_category)
            index_category+=1
            index_product = 0
            for category in range(0, 20):
                category = Category().get_category(url_category, index_product)
                list_category.append(category)
                set_category = set(list_category)
                print(f"filter: {set_category}")
            for category in set_category:
                print(category)
                category = Category(pnns_groups_1=category)
                category.save()
        
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

Product.fill_nutriscore_database()
#Product.fill_init_category_database()
Product.fill_category_database()
Product.fill_product_database()