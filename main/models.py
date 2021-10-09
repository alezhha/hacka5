from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='', blank=True, null=True)
    image = models.ImageField(upload_to = 'upload/products')

class Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.CharField(max_length=1000)