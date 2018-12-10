from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_lenght=50, blank=False)
    phone_number =models.CharField(max_lenght=20, blank=False)
    country = models.CharField(max_lenght=40, blank=False)
    postcode = models.CharField(max_lenght=20, blank=True)
    town_or_city = models.CharField(max_lenght=40, blank=False)
    street_address1 = models.CharField(max_lenght=40, blank=False)
    street_address2 = models.CharField(max_lenght=40, blank=False)
    county = models.CharField(max_lenght=40, blank=False)
    date =  models.DateField()

    def __self__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
# Rerurning a string which is a sumamry of the order

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __self__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
# Return a string of the individual order line