from django.test import TestCase
from products.models import Product, Category


# """Create your tests here. Créer un model product avec les attributs: 
class TestCreateUser(TestCase):
    def testCreateProduct(self):
        product = Product(product_name='Crème de noisette',
                       nutriscore_grade= 'c',
                       image_url='https://images.openfoodfacts.org/images/products/361/304/271/7385/front_fr.3.400.jpg',
                       pnns_groups_1= Category("Fruits and vegetables"),
                       ingredients_text="Poudre de NOISETTE, eau, sucre de canne, sirop de glucose-fructose, gélifiant : pectine de fruits.",
                       url="https://fr.openfoodfacts.org/produit/3613042717385/creme-de-noisette-phil-gourmet")
        self.assertEqual(product.product_name, 'Crème de noisette')
        self.assertEqual(product.nutriscore_grade, 'c')
        self.assertEqual(product.image_url, 'https://images.openfoodfacts.org/images/products/361/304/271/7385/front_fr.3.400.jpg')
        self.assertEqual(product.pnns_groups_1, Category("Fruits and vegetables")),
        self.assertEqual(product.ingredients_text, "Poudre de NOISETTE, eau, sucre de canne, sirop de glucose-fructose, gélifiant : pectine de fruits."),
        self.assertEqual(product.url, "https://fr.openfoodfacts.org/produit/3613042717385/creme-de-noisette-phil-gourmet")
