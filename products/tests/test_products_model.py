from spaceUser.models import User
from products.models import Favorites, Product, Category

import pytest


class TestProductsModel:
    @pytest.mark.django_db
    def test_product_model(self):
        """
        We are creating a Product object, a user object and also a temporary
        user to pass Login Check, Then we are creating a FavouriteProduct
        object and testing if our is_favourite method is properly working
        """
        category_vegetale = Category.objects.create(pnns_groups_1="vegetale")
        product = Product.objects.create(
            product_name='Crème de noisette',
            nutriscore_grade='c',
            image_url='https://images.openfoodfacts.org/images/products/361/304/271/7385/front_fr.3.400.jpg', # noqa
            pnns_groups_1=category_vegetale,
            ingredients_text="""Poudre de NOISETTE, eau, sucre de canne,
            sirop de glucose-fructose, gélifiant : pectine de fruits.""",
            url="https://fr.openfoodfacts.org/produit/3613042717385/creme-de-noisette-phil-gourmet") # noqa
        assert str(product) == f"{product.url}"

    @pytest.mark.django_db
    def test_category_model(self):
        """
        Wr are creating a Category object, a user object and also a
        temporary user to pass Login Check, Then we are creating a
        FavouriteProduct object and testing if our is_favourite
        method is properly working
        """
        category_vegetale = Category.objects.create(pnns_groups_1="vegetale")
        assert str(category_vegetale) == f"{category_vegetale.pnns_groups_1}"

    @pytest.mark.django_db
    def test_favorite_model(self):
        """
        Wr are creating a Category object, a user object and
        also a temporary user to pass Login Check, Then we are creating
        a FavouriteProduct object and testing if our
        is_favourite method is properly working
        """
        user = User.objects.create(username="user", email="user@user.com")
        category_vegetale = Category.objects.create(pnns_groups_1="vegetale")
        product = Product.objects.create(
            product_name='Crème de noisette',
            nutriscore_grade='c',
            image_url='https://images.openfoodfacts.org/images/products/361/304/271/7385/front_fr.3.400.jpg', # noqa
            pnns_groups_1=category_vegetale,
            ingredients_text="""Poudre de NOISETTE, eau, sucre de canne,
            sirop de glucose-fructose, gélifiant : pectine de fruits.""",
            url="https://fr.openfoodfacts.org/produit/3613042717385/creme-de-noisette-phil-gourmet") # noqa
        favorite = Favorites.objects.create(user=user, product=product)
        assert str(favorite) == f"{favorite.user} -> {favorite.product}"
