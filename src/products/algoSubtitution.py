from django.contrib.postgres.search import SearchVector
from products.models import Product

class AlgoSubtitution:
    def __init__(self, keyword:str) -> None:
        self.keyword = keyword
        self.result_search = self.search_products()
        #self.caracteristiques_substitution = self.get_caracteristiques_substitution()
        #self.category = self.get_category_of_product(self.result_search)
        #self.list_products = self.get_list_products_of_category_after_search()
        #self.substitution = self.get_best_product_for_its_category()
    
    def search_products(self):
        search = SearchVector("product_name") + SearchVector("ingredients_text") + SearchVector("url") + SearchVector("pnns_groups_1")
        result_search = Product.objects.annotate(search=search).filter(search=self.keyword).order_by("nutriscore_grade")
        return result_search
    
    #def get_caracteristiques_substitution(self, substitution):
    #    caracteristiques_substitution = Product.objects.get()
    #    return caracteristiques_substitution
    
    #def get_category_of_product(self, product):
    #    category = Product.objects.get(pnns_groups_1=product)
    #    return category
    
    #def get_list_products_of_category_after_search(self):
    #    list_products = Product.objects.filter(product_name__icontains=self.keyword)
    #    print(f"list products: {list_products}")
    #    return list_products

    #def get_best_product_for_its_category(self):
    #    substitution = Product.objects.filter(self.category).order_by("pnns_groups_1")[0]
    #    return substitution