from django.db import models

#USER E-WALLET
class ewallet(models.Model):
    walletID = models.IntegerField(primary_key=True)
    walletPass = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.BooleanField()

class recovery_codes(models.Model):
    codeID = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=6)
    status = models.BooleanField()
    walletID = models.IntegerField()

class ewallet_transaction(models.Model):
    transactionID = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transactionType = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    walletID = models.IntegerField()
    orderID = models.IntegerField()
