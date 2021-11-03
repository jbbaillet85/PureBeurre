from django.test import Client
import pytest

client = Client()


@pytest.mark.django_db
class TestProductsViews:

    def test_get_results_products_views(self):
        response = client.post('/products/result_products',
                               {'search_product': 'pizza'})
        assert response.status_code == 200

    def test_get_choice_substitution_views(self):
        response = client.post(
            '/products/description_product', {'product_id': '1'})
        assert response.status_code == 302
