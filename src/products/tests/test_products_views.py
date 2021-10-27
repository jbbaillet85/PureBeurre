from django.urls import reverse 
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest

@pytest.mark.django_db
class TestProductsViews:
    client = Client()

    def test_get_results_products_views(self):
        response = self.client.post('/products/result_products', {'search_product':'pizza'})
        assert response.status_code == 200
    
    def test_get_choice_substitution_views(self):
        pass