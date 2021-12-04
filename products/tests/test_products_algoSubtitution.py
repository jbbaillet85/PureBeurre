from spaceUser.models import User
from products.models import Product, Category
from products.algoSubtitution import Substitution, ProductsOfFavorites
from django.test import Client

import pytest


class TestAlgoSustitution:
    @pytest.mark.django_db
    def test_algoSubsitition(self):
        client = Client()
        user = User.objects.create(
            last_name='jb', email='user@mail.com', password='password')
        client.force_login(user)
        category_vegetale = Category.objects.create(pnns_groups_1="vegetale")
        product = Product.objects.create(id=1, pnns_groups_1=category_vegetale)
        algo = Substitution(product.id)
        assert str(
            algo) == f"category: {algo.category} - products: {algo.list_products}" # noqa

    @pytest.mark.django_db
    def test_ProductsOfFavorites(self):
        client = Client()
        user = User.objects.create(username='jb',
            last_name='jb', email='user@mail.com', password='password')
        client.force_login(user)
        algo = ProductsOfFavorites(user.id)
        assert str(
            algo) == f"favorite: user: {algo.id_user} - products: {algo.products}" # noqa
