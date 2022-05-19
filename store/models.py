from django.db import models
from django.utils import timezone as tz
from datetime import date, time

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name(self)
    
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    media = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.CharField(max_length=254, null=True, blank=True)
    user_id = models.CharField(max_length=254, null=True, blank=True)
    transaction_date = models.DateField(default=tz.now)
    transaction_time = models.TimeField(default=time(18, 00))
    grand_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)


class Bag(models.Model):
    bag_items = models.IntegerField(default=0)
    bag_name = models.CharField(max_length=254, null=True, blank=True, default="guest")
