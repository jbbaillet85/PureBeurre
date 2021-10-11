from django.contrib.postgres.search import SearchVector
from products.models import Product, Favorites
from spaceUser.models import User

class AlgoSubtitution:
    def __init__(self, keyword:str) -> None:
        self.keyword = keyword
        self.result_search = self.search_products()
    
    def search_products(self):
        search = SearchVector("product_name") + SearchVector("ingredients_text") + SearchVector("url") + SearchVector("pnns_groups_1")
        result_search = Product.objects.annotate(search=search).filter(search=self.keyword).order_by("nutriscore_grade")
        return result_search

class Substitution:
    def __init__(self, product_id) -> None:
        self.product_id = product_id
        self.category = self.get_category_of_product()
        self.list_products = self.get_list_products_of_category_after_search()

    def get_category_of_product(self):
        category = Product.objects.get(id=self.product_id)
        return category.pnns_groups_1
    
    def get_list_products_of_category_after_search(self):
        list_products = Product.objects.filter(pnns_groups_1=self.category).exclude(pnns_groups_1="0").order_by("nutriscore_grade")[:6]
        print(f"list products: {list_products}")
        return list_products
    
class ProductsOfFavorites:
    def __init__(self, id_user) -> None:
        self.id_user = id_user
        self.products = self.get_products_of_favorites()

    def get_products_of_favorites(self):
        products = []
        favorites = Favorites.objects.filter(user=self.id_user)
        for favorite in favorites:
            product = Product.objects.get(id=favorite.product_id)
            products.append(product)
        return products
        