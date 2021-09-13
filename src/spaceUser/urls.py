from django.urls import path

from spaceUser.views import identification, register, identification, spaceUser

urlpatterns = [
    path('register', register, name='register'),
    path('login', identification, name='login'),
    path('spaceUser', spaceUser, name='spaceUser'),
]