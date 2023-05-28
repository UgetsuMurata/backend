from django.db import models

#USER
class user(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=11)

class user_info(models.Model):
    UserID = models.IntegerField(max_length=11)
    lName = models.CharField(max_length=20)
    fName = models.CharField(max_length=20)
    mInit = models.CharField(max_length=1)
    street = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

#USER E-WALLET
class ewallet(models.Model):
    walletID = models.IntegerField(max_length=11)
    walletPass = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.BooleanField()

class recovery_codes(models.Model):
    codeID = models.IntegerField(max_length=11)
    code = models.CharField(max_length=6)
    status = models.BooleanField()

class ewallet_transaction(models.Model):
    transactionID = models.IntegerField(max_length=11)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transactionType = models.IntegerField(max_digits=1)
    date = models.DateField(auto_now_add=True)

#POINTS
class points(models.Model):
    pointID = models.IntegerField(max_length=11)
    barcode = models.CharField(max_length=12)
    totalPoints = models.IntegerField(max_length=3)

class points_transaction(models.Model):
    transactionID = models.IntegerField(max_length=11)
    pointsReduced = models.IntegerField(max_length=11)
    date = models.DateField(auto_now_add=True)

class reward(models.Model):
    rewardID = models.IntegerField(max_length=11)
    requiredPoints = models.IntegerField(max_length=3)
    rewardExpDate = models.DateField()

#ORDER
class order(models.Model):
    orderID = models.IntegerField(max_length=11)
    status = models.IntegerField(max_length=1)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentType = models.IntegerField(max_length=1)
    date = models.DateField(auto_now_add=True)

class order_items(models.Model):
    itemID = models.IntegerField(max_length=11)
    quantity = models.IntegerField(max_length=3)

class products(models.Model):
    productID = models.IntegerField(max_length=11)
    productCategory = models.CharField(max_length=20)
    productName = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    productImage = models.BooleanField()

class food(products):
    unit = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    status = models.IntegerField(max_length=1)

class drink(products):
    flavor = models.CharField(max_length=50)
    cupSize = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    status = models.IntegerField(max_length=1)