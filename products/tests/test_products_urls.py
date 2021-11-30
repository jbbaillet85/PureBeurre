from django.urls import reverse, resolve
from products.views import get_choice_substitution, get_description_product
from products.views import get_favorites, get_results_products


class TestProductsUrls:
    def test_result_products_url(self):
        """ Testing if the 'result_products' route maps to
        our 'result_products' view """

        url = reverse('result_products')
        assert resolve(url).view_name == 'result_products'
        assert resolve(url).func, get_results_products

    def test_choice_subtitution_url(self):
        """ Testing if the 'caracteristiques_subtitution' route maps
        to our 'caracteristiques_subtitution' view """

        url = reverse('choice_subtitution')
        assert resolve(url).view_name == 'choice_subtitution'
        assert resolve(url).func, get_choice_substitution

    def test_description_product_url(self):
        """ Testing if the 'description_product' route maps to
        our 'description_product' view """

        url = reverse('description_product')
        assert resolve(url).view_name == 'description_product'
        assert resolve(url).func, get_description_product

    def test_favorites_url(self):
        """ Testing if the 'favorites' route maps to our 'favorites' view """

        url = reverse('favorites')
        assert resolve(url).view_name == 'favorites'
        assert resolve(url).func, get_favorites
