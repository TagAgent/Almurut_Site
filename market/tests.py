from datetime import datetime
from itertools import product

from django.test import TestCase
from unicodedata import category

from market.models import ProductCategory, Product


class ProductListTestCase(TestCase):

    def test_product_list_success(self):
        response = self.client.get('/product-list/')

        self.assertEqual(response.status_code, 200)

class ProductDetailTestCase(TestCase):

    def test_product_detail_success(self):
        some_date = datetime(year=2024, month=11, day=10)

        cat1 = ProductCategory.objects.create(name='Tea doll boy ob')

        product = Product.objects.create(
            category=cat1,
            name='Pineapple Watch v sry raza doroje',
            price=15000,
            sales_percent=0,
            description='Huje Redmi no v sry raza doroje apple',
            new_expiry_date=some_date,
            preview_image='/media/kartinca.jpeg'
        )

        response = self.client.get(f'/product-detail/{product.id}/')

        self.assertEqual(response.status_code, 200)
