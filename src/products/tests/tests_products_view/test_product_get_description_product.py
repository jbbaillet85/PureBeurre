from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from spaceUser.models import User
from products.models import Category, Product
import pytest


class TestProductsViews:

    @pytest.mark.django_db
    def test_get_description_product_views(self):
        client = Client()
        user = User.objects.create(
            last_name='jb', email='user@mail.com', password='password')
        client.force_login(user)
        category_vegetale = Category.objects.create(pnns_groups_1="vegetale")
        product = Product.objects.create(id=1, pnns_groups_1=category_vegetale)
        response = client.post(
            '/products/description_product', {'product_id': product.id})
        assert response.status_code == 200