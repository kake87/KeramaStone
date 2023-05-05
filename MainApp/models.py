from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products')


class Travertin(models.Model):
    name = models.CharField(max_length=255, verbose_name='Марка травертина')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(verbose_name='Стоимость товара', max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='Прикрепите изображение', upload_to='static/images/products/travertin/')
    published = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=False, verbose_name='В наличии')
    order_only = models.BooleanField(default=False, verbose_name='Под заказ')

    def __str__(self) -> str:
        return self.name
    
class Granit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Марка гранита')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(verbose_name='Стоимость товара', max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='Прикрепите изображение', upload_to='static/images/products/granit/')
    published = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=False, verbose_name='В наличии')
    order_only = models.BooleanField(default=False, verbose_name='Под заказ')

    def __str__(self) -> str:
        return self.name

class Mramor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Марка мрамора')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(verbose_name='Стоимость товара', max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='Прикрепите изображение', upload_to='static/images/products/mramor/')
    published = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=False, verbose_name='В наличии')
    order_only = models.BooleanField(default=False, verbose_name='Под заказ')
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class Request(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя: ')
    phone_number = models.CharField(max_length=21, verbose_name='Номер телефона: ')
    email = models.EmailField(verbose_name='Электронная почта: ')
    text_box = models.TextField()
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания: ')

    def __str__(self):
        return f"{self.name}-{self.email}-{self.phone_number}"