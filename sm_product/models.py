from django.db import models


class Category(models.Model):
    name = models.CharField("Группа товара", max_length=64)

    @classmethod
    def price_gte_count(cls, price):
        return cls.objects.filter(product__price__gte=price).annotate(total_categories=models.Count('pk')).values()

    @classmethod
    def products_gt_count(cls, num):
        return cls.objects.annotate(product_count=models.Count('product')).filter(product_count__gt=num)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Группа")
    name = models.CharField("Название товара", max_length=128)
    price = models.DecimalField("Стоимость единицы, руб.", max_digits=10, decimal_places=2)

    @classmethod
    def with_category(cls):
        return cls.objects.select_related('category').all()


class Person(models.Model):
    name = models.CharField('Item', max_length=100)
    birthday = models.DateField('Birthday', null=True, blank=False)


# B
class CustomQuerySet(models.QuerySet):
    def delete(self):
        self.update(active=False)

    def delete_real(self):
        super(CustomQuerySet, self).delete()


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


class Item(models.Model):
    name = models.CharField('Item', max_length=100)
    active = models.BooleanField('Active', default=True)
    objects = CustomManager()


"""
CREATE TABLE phones (phone varchar, users int[]);
CREATE TABLE items (id serial, user_id int, status smallint);
SELECT count(*) FROM items JOIN phones ON items.user_id = ANY (phones.users) WHERE phones.phone='3141592' AND items.status=7;
SELECT count(*) FROM items JOIN phones ON items.user_id = ANY (phones.users) WHERE phones.phone='3141592' AND items.status IN (3,7);
"""
