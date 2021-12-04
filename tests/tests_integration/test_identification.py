import pytest

from django.urls import reverse
from django.test import Client
from django.contrib import auth


@pytest.mark.django_db
def test_register_identification_logout():
    client = Client()

    # Register a user using the `register` view
    # in order to register it in the database
    credentials = {
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword',
    }
    temp_user = client.post(reverse('register'), credentials) # noqa

    # Connect this user with the `login` view
    response = client.post(
        reverse('login'), {'email': 'testuser@testing.com', 'password': 'TestPassword'})

    # Check that the redirection to the home page is done
    assert response.status_code == 200

    # Check that the user is properly authenticated
    user = auth.get_user(client)
    assert user.is_authenticated
