
from django.urls import reverse, resolve

from spaceUser.views import register, identification, spaceUser, logout


class TestSpaceUserUrls:
    def test_register_url(self):
        """
        Testing if the 'register' route maps to register
        """

        url = reverse('register')
        assert resolve(url).view_name == 'register'
        assert resolve(url).func, register

    def test_identification_url(self):
        """
        Testing if the 'identification' route maps to login
        """

        url = reverse('login')
        assert resolve(url).view_name == 'login'
        assert resolve(url).func, identification

    def test_spaceUser_url(self):
        """
        Testing if the 'spaceUser' route maps to spaceUser
        """

        url = reverse('spaceUser')
        assert resolve(url).view_name == 'spaceUser'
        assert resolve(url).func, spaceUser

    def test_logout_url(self):
        """
        Testing if the 'spaceUser' route maps to spaceUser
        """

        url = reverse('logout')
        assert resolve(url).view_name == 'logout'
        assert resolve(url).func, logout
