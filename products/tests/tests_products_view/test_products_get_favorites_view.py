from django.test import Client
from spaceUser.models import User
from products.models import Category, Product
import pytest


class TestProductsViews:

    @pytest.mark.django_db
    def test_get_get_favorites_views(self):
        client = Client()
        user = User.objects.create(
            last_name='jb', email='user@mail.com', password='password')
        client.force_login(user)
        category_vegetale = Category.objects.create(pnns_groups_1="vegetale")
        product = Product.objects.create(id=1, pnns_groups_1=category_vegetale)
        response = client.post('/products/favorites',
                               {'product_id': product.id})
        assert response.status_code == 200
