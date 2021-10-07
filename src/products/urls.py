from django.urls import path

from products.views import get_results_products, get_caracteristiques_substitution, get_description_product

urlpatterns = [
    path('result_products', get_results_products, name='result_products'),
    path('caracteristiques_subtitution', get_caracteristiques_substitution, name='caracteristiques_subtitution'),
    path('description_product', get_description_product, name='description_product'),
]