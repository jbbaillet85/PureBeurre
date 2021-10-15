from django.urls import reverse 
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest


class TestProductsViews:
    client = Client()
    
    @pytest.mark.django_db
    def test_results_products_views(self):
        response = self.client.get(reverse('result_products'))

        """ 
        In the first assert, We are testing if our get request returns 200 (OK) status code 
        For the second assert, we are making sure that our view returns the result_products.html template
        """
        
        assert response.status_code == 200
        assertTemplateUsed(response, 'result_products.html')