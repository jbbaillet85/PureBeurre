import pytest
from django.template import context
from django.test import Client, TestCase
from django.urls import resolve, reverse
from products.algoSubtitution import AlgoSubtitution
from pytest_django.asserts import assertTemplateUsed
from homepage.forms import SearchForm


class TestHomepageViews(TestCase):
    client = Client()

    @pytest.mark.django_db
    def test_HomePage_View(self):

        """
        Testing if HomePage is properly rendered with 200 status code and in second assert,
        we are making sure it returns the correct template 'homepage.html'
        """

        temp_user = self.client.post('/homepage/')

        response = self.client.get(reverse('homepage'))
        
        assert response.status_code == 200
        assertTemplateUsed(response, 'homepage.html')
        
    @pytest.mark.django_db
    def test_HomePage_result_products_View(self):
        keyword = 'pizza'
        temp_user = self.client.post('/products/result_products', {'search_product':keyword})
        response = self.client.get(reverse('result_products'))
        products = AlgoSubtitution(keyword)
        context = {'search_product':keyword, 'products':products.result_search}
        assert response.status_code == 200
        #assertTemplateUsed(response, 'result_products.html', context)
    
    @pytest.mark.django_db
    def test_mentions_legales_View(self):

        """
        Testing if mentions_legales is properly rendered with 200 status code and in second assert,
        we are making sure it returns the correct template 'mentions_legales.html'
        """

        temp_user = self.client.post('/mentions_legales/')

        response = self.client.get(reverse('mentions_legales'))
        
        print(response)
        assert response.status_code == 200
        assertTemplateUsed(response, 'mentions_legales.html')
