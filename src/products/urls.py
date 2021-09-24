from django.urls import path

from products.views import get_products

urlpatterns = [
    path('result_products', get_products, name='result_products'),
]