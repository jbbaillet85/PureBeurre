from django.urls import path

from homepage.views import homepage, mentions_legales

urlpatterns = [
    path('', homepage, name='homepage'),
    path('mentions_legales', mentions_legales, name='mentions_legales'),
]
