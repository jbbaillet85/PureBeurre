from django.test import Client
from products.models import Product, Category
import pytest


class TestProductsViews:

    @pytest.mark.django_db
    def test_get_choice_substitution_views(self):
        client = Client()
        category_vegetale = Category.objects.create(pnns_groups_1="vegetale")
        product = Product.objects.create(id=1, pnns_groups_1=category_vegetale)
        response = client.post(
            '/products/choice_subtitution', {'product_id': product.id})
        assert response.status_code == 200
