from django.db import models

class points(models.Model):
    pointID = models.IntegerField(primary_key=True)
    barcode = models.CharField(max_length=12)
    totalPoints = models.IntegerField()

class points_transaction(models.Model):
    transactionID = models.IntegerField(primary_key=True)
    pointsReduced = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    pointID = models.IntegerField()
    rewardID = models.IntegerField()
    walletID = models.IntegerField()

class reward(models.Model):
    rewardID = models.IntegerField(primary_key=True)
    requiredPoints = models.IntegerField()
    rewardExpDate = models.DateField()
    productID = models.IntegerField()
