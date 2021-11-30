import pytest
from django.test import Client, TestCase
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


class TestHomepageViews(TestCase):
    client = Client()

    @pytest.mark.django_db
    def test_HomePage_View(self):
        """
        Testing if HomePage is properly rendered with 200 status code
        and in second assert,
        we are making sure it returns the correct template 'homepage.html'
        """
        response = self.client.get(reverse('homepage'))
        assert response.status_code == 200
        assertTemplateUsed(response, 'homepage.html')

    @pytest.mark.django_db
    def test_HomePage_result_products_View(self):
        response = self.client.get(reverse('result_products'))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_mentions_legales_View(self):
        """
        Testing if mentions_legales is properly rendered with 200 status code
        and in second assert,
        we are making sure it returns the correct template
        'mentions_legales.html'
        """
        response = self.client.get(reverse('mentions_legales'))
        assert response.status_code == 200
        assertTemplateUsed(response, 'mentions_legales.html')
