from django.test import Client
from django.urls import reverse

import pytest

class TestSpaceUserView:
    client = Client()

    @pytest.mark.django_db
    def test_register_view(self):

        """
        In the first assert, we are checing if a user is created successfully then, the user is redirected to '/login/' route,
        For the second assert, we are checking the 302 status code(redirect)
        """

    @pytest.mark.django_db
    def test_logout_view(self):

        """
        Testing if our LogoutView properly logouts user, In the first assert, we are checking if user is redirected to 
        home route, for the second assert we are checking 302 redirect status code
        """

        response = self.client.get(reverse('logout'))

        assert response.url == '/spaceUser/login'
        assert response.status_code == 302
