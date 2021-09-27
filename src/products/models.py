from django.db import models

class Category(models.Model):
    pnns_groups_1 = models.CharField(max_length=150, default="0", unique=True)
    
    def __str__(self) -> str:
        return self.pnns_groups_1

class Product(models.Model):
    product_name= models.CharField(max_length=150, default="pas de nom de produit")
    nutriscore_grade=models.CharField(max_length=1, default="0")
    image_url=models.ImageField(default="")
    pnns_groups_1=models.ManyToManyField(Category)
    ingredients_text=models.TextField(default="pas d'ingrédients renseignés")
    url=models.URLField(unique=True)
    
    def __str__(self) -> str:
        return self.url
