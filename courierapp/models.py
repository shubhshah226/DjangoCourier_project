from django.db import models

# Create your models here.
class RegModels(models.Model):
	Username=models.CharField(max_length=50)
	Password=models.CharField(max_length=50)
	Eid=models.CharField(max_length=50)
	def __str__(self):
		return self.Username

class BackendModel(models.Model):
	origin=models.CharField(max_length=20)
	companyname=models.CharField(max_length=20)
	date=models.CharField(max_length=20)
	time=models.TimeField()
	destination=models.CharField(max_length=20)
	noteno=models.CharField(max_length=20)
	def __str__(self):
		return self.destination

class Member(models.Model):
	FirstName = models.CharField(max_length=120)
	LastName = models.CharField(max_length= 120)
	PhoneNumber = models.CharField(max_length= 120)
	Email = models.CharField(max_length= 120)
	Password=models.CharField(max_length= 120)
	def __str__(self):
		return self.FirstName

class cmpModel(models.Model):
	Context = models.CharField(max_length=500)
	PhoneNumber=models.CharField(max_length=10)
	Email=models.CharField(max_length=20)
	def __str__(self):
		return self.Email