from django.db import models

# Create your models here.
class Device(models.Model):

	item = models.CharField(max_length=100)
	price = models.IntegerField()
	choices = (
		('AVAILABLE','Item ready to be purchased'),
		('SOLD','Sold out'),
		('RESTOCKING','Item will restoking in few days')

		)
	status = models.CharField(max_length=250,choices=choices,default='SolD')
	issues = models.CharField(max_length=250,default='No issues')

	class Meta:
		abstract = True

	def __str__(self):
		return self.item 

class Laptop(Device):
	pass

class Desktop(Device):
	pass

class Mobile(Device):
	pass

