import pytest

from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from django.test import Client
from django.contrib import auth
from spaceUser.views import register, identification


@pytest.mark.django_db
def test_register_identification_logout():
    client = Client()

    # Inscrire un utilisateur à l’aide de la vue `register`afin de l’enregistrer dans la base de données
    credentials = {
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = client.post(reverse('register'), credentials)

    # Connecter cet utilisateur avec la vue `login`
    response = client.post(
        reverse('login'), {'username': 'TestUser', 'password': 'TestPassword'})

    # Vérifier que la redirection vers la page d’accueil est effectuée
    assert response.status_code == 200
    #assert response.url == reverse('spaceUser')

    # Vérifier que l’utilisateur est bien authentifié
    user = auth.get_user(client)
    assert user.is_authenticated
