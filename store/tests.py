from django.test import TestCase
from store.models import Category, Product, Order, Bag
from store.forms import OrderForm
from django.utils import timezone as tz
from datetime import date, time
from django.shortcuts import reverse


# Models test
class CategoryProductTest(TestCase):

    def create_category(self, name="Clothing", friendly_name="Clothes for sale" ):
        return Category.objects.create(name=name, friendly_name=friendly_name)

    def create_product(self, category, sku="p100", name="T-Shirt",\
                        description="Comfy T Shirt", has_sizes=True, price=100,rating=5,\
                        image_url=None,image=None,media=None):

        return Product.objects.create(category=category,sku=sku,name=name,description=description,\
                                        has_sizes=has_sizes,price=price,rating=rating,image_url=image_url,\
                                        image=image,media=media)        
    
    def test_category_product_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.name)

        p = self.create_product(category=c)
        self.assertTrue(isinstance(p, Product))
        self.assertEqual(p.__str__(), p.name)

    
    
  
class OrderTest(TestCase):

    def create_order(self, order_id="1234", order_items="1 2 3 4", user_id="guest", \
                        transaction_date=tz.now(), transaction_time=time(18,00), grand_total=100.00):
        return Order.objects.create(order_id=order_id,order_items=order_items,user_id=user_id,\
                                    transaction_date=transaction_date,transaction_time=transaction_time,\
                                    grand_total=grand_total)
    
    def test_order_creation(self):
        o = self.create_order()
        self.assertTrue(isinstance(o, Order))

class BagTest(TestCase):

    def create_bag(self, bag_items="1 2 3", bag_quantity=3 ):
        return Bag.objects.create(bag_items=bag_items, bag_quantity=bag_quantity)

    
    def test_bag_creation(self):
        b = self.create_bag()
        self.assertTrue(isinstance(b, Bag))
        





