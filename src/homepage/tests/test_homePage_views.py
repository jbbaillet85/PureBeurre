from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

class TestHomepageViews:
    client = Client()

    @pytest.mark.django_db
    def test_HomePage_View(self):

        """
        Testing if HomePage is properly rendered with 200 status code and in second assert,
        we are making sure it returns the correct template 'homepage.html'
        """

        temp_user = self.client.post('/homepage/')

        response = self.client.get(reverse('homepage'))
        
        print(response)
        assert response.status_code == 200
        assertTemplateUsed(response, 'homepage.html')

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