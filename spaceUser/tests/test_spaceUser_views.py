from django.test import Client
from django.urls import reverse

import pytest


class TestSpaceUserView:
    client = Client()

    @pytest.mark.django_db
    def test_register_view(self):
        """
        In the first assert, we are checing if a user is created successfully
        then,the user is redirected to '/spaceUser/' route,
        For the second assert, we are checking the 302 status code(redirect)
        """
        TestSpaceUserView.client.post('register', {
            'username': 'username', 'last_name': 'last_name',
            'email': 'email@email.com',
            'password1': 'password', 'password2': 'password'})

    @pytest.mark.django_db
    def test_spaceUser_view(self):
        """
        Testing spaceUser
        """

        response = self.client.get(reverse('spaceUser'))

        assert response.url == '/accounts/login/?next=/spaceUser/spaceUser'
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_logout_view(self):
        """
        Testing if our LogoutView properly logouts user, In the first assert,
        we are checking if user is redirected to
        home route, for the second assert we are checking 302 redirect
        status code
        """

        response = self.client.get(reverse('logout'))

        assert response.url == '/spaceUser/login'
        assert response.status_code == 302
