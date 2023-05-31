from django.db import models

class user(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=11)
    
class userHasInfo(models.Model):
    userID = models.IntegerField( primary_key=True)
    email = models.CharField(max_length=200)
    fullname = models.IntegerField()
    fullAddress = models.IntegerField()

class user_info(models.Model):
    userID = models.IntegerField(primary_key=True)
    lName = models.CharField(max_length=20)
    fName = models.CharField(max_length=20)
    mInit = models.CharField(max_length=1)
    street = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

class userCreatesEwallet(models.Model):
    userID = models.IntegerField(primary_key=True)
    walletID = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class userReceivesPoints(models.Model):
    userID = models.IntegerField(primary_key=True)
    pointID = models.IntegerField()
    date = models.DateField(auto_now_add=True)
