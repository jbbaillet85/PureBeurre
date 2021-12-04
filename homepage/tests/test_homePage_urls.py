from django.urls import reverse, resolve
from homepage.views import homepage, mentions_legales


class TestHomepageUrls:
    def test_homepage_url(self):
        """ Testing if the 'homepage' route maps to our 'homepage' view """

        url = reverse('homepage')
        assert resolve(url).view_name == 'homepage'
        assert resolve(url).func, homepage

    def test_mentions_legales_url(self):
        """ Testing if the 'mentions_legales' route maps
        to our 'mentions_legales' view """

        url = reverse('mentions_legales')
        assert resolve(url).view_name == 'mentions_legales'
        assert resolve(url).func, mentions_legales
