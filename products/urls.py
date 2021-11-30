from django.urls import path

from products.views import get_results_products, get_choice_substitution
from products.views import get_description_product, get_favorites

urlpatterns = [
    path('result_products', get_results_products, name='result_products'),
    path('choice_subtitution', get_choice_substitution,
         name='choice_subtitution'),
    path('description_product', get_description_product,
         name='description_product'),
    path('favorites', get_favorites, name='favorites'),
]
