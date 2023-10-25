import requests

from django.core.management import BaseCommand
from django.utils.text import slugify
from ...models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Creating data......')
        response = requests.get('https://fakestoreapi.com/products').json()

        for product in response:
            category, _ = Category.objects.get_or_create(
                title = product['category'],
                slug = slugify(product['category']),
                featured = True
            )
            Product.objects.create(
                category = category,
                title = product['title'],
                slug = slugify(product['title']),
                discription = product['description'],
                price = product['price'],
                thumbnail = product['image']
            )
        print('Creating data Succesfully! you can use them now!')