from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    address_line_1 = models.CharField(max_length=40, blank=False)
    address_line_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date =  models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
# Returning a string which is a summary of the order


class OrderLineItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, 
                                      self.product.price)
# Return a string of the individual order line
