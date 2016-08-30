from django.core.management.base import BaseCommand
from ...models import Category, Product
from decimal import Decimal
from pprint import pprint


class Command(BaseCommand):
    # Django command help
    help = 'Задание начальных данных для моделей в БД.'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        Category.objects.bulk_create([
            Category(name=name) for name in ('Воланы', 'Ракетки', 'Мячи', 'Обувь')
        ])
        categories = {category.name: category for category in Category.objects.all()}

        Product.objects.bulk_create([
            Product(**prod) for prod in (
                {
                    'category': categories['Воланы'],
                    'name': 'Yonex 2000',
                    'price': Decimal('10')
                },
                {
                    'category': categories['Воланы'],
                    'name': 'Victor 1000',
                    'price': Decimal('30')
                },
                {
                    'category': categories['Воланы'],
                    'name': 'Adidas 500',
                    'price': Decimal('20')
                },
                {
                    'category': categories['Ракетки'],
                    'name': 'Yonex ArcSaber 7',
                    'price': Decimal('7000')
                },
                {
                    'category': categories['Ракетки'],
                    'name': 'Victor BraweSword 12',
                    'price': Decimal('8000')
                },
                {
                    'category': categories['Ракетки'],
                    'name': 'Babolat Drive Tour',
                    'price': Decimal('12500')
                },
                {
                    'category': categories['Ракетки'],
                    'name': 'Adidas PrecisionPro',
                    'price': Decimal('5000')
                },
                {
                    'category': categories['Мячи'],
                    'name': 'Wilson Tour Davis',
                    'price': Decimal('300')
                },
                {
                    'category': categories['Мячи'],
                    'name': 'Prince Futures',
                    'price': Decimal('200')
                },
                {
                    'category': categories['Мячи'],
                    'name': 'Dunlop Hard court',
                    'price': Decimal('100')
                },
                {
                    'category': categories['Обувь'],
                    'name': 'Adidas Fast Run 01',
                    'price': Decimal('7000')
                },
                {
                    'category': categories['Обувь'],
                    'name': 'Adidas Fast Run 02',
                    'price': Decimal('8000')
                },
            )
        ])

        print('\nCount of products which have price bigger than 100 grouped by category')
        [pprint(category) for category in Category.price_gte_count('100').values()]

        print('\nCategories which have more than two products')
        [pprint(category) for category in Category.products_gt_count(2).values()]

        print('\nRetrieve products and their categories in one query')
        print(Product.with_category().query)
        for product in Product.with_category():
            print('{} {} {}'.format(product.category.name, product.name, product.price))
