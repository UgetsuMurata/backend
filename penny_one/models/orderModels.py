from django.db import models

class order(models.Model):
    orderID = models.AutoField(primary_key=True)
    status = models.IntegerField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentType = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    userID = models.IntegerField()

class order_items(models.Model):
    itemID = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    productID = models.IntegerField()
    orderID = models.IntegerField()

class products(models.Model):
    productID = models.CharField(max_length=12, primary_key=True)
    productCategory = models.CharField(max_length=20)
    productName = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    productImage = models.URLField()
    isFeatured = models.BooleanField()
    details = models.TextField(null=True, blank=True)

class food(models.Model):
    unit = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField()
    prodfk = models.ForeignKey(products, on_delete=models.CASCADE)

class drink(models.Model):
    flavor = models.CharField(max_length=50)
    isSpecialty = models.BooleanField()
    cupSize = models.CharField(max_length=10) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField()
    prodfk = models.ForeignKey(products, on_delete=models.CASCADE)