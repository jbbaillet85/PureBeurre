from django.urls import path

from spaceUser.views import register, login, spaceUser

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('spaceUser', spaceUser, name='spaceUser'),
]