from django.db import models

class order(models.Model):
    orderID = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentType = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    userID = models.IntegerField()

class order_items(models.Model):
    itemID = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    productID = models.IntegerField()
    orderID = models.IntegerField()

class products(models.Model):
    productID = models.AutoField(primary_key=True)
    productCategory = models.CharField(max_length=20)
    productName = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    productImage = models.BooleanField()
    status = models.IntegerField()

class food(products):
    unit = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()

class drink(products):
    flavor = models.CharField(max_length=50)
    cupSize = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
