from django.db import models

class workerPortal(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    accountType = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=11)

class workerHasDP(models.Model):
    email = models.EmailField()
    dpId = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    fullname = models.CharField(max_length=50)

class deliveryPersonnel(models.Model):
    dpId = models.IntegerField(primary_key=True)
    lName = models.CharField(max_length=20)
    fName = models.CharField(max_length=20)
    mInit = models.CharField(max_length=1)
    branchID = models.IntegerField()

class workerHasBranch(models.Model):
    email = models.EmailField(max_length=200)
    branchID = models.IntegerField()
    fullAddress = models.IntegerField()

class branch(models.Model):
    branchID = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    zipCode = models.IntegerField()