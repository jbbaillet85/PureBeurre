from django.urls import path

from spaceUser.views import identification, register, spaceUser, logout_user

urlpatterns = [
    path('register', register, name='register'),
    path('login', identification, name='login'),
    path('logout', logout_user, name='logout'),
    path('spaceUser', spaceUser, name='spaceUser'),
]
