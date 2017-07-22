from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 20)
	phone_number = models.CharField(max_length = 15)
	address = models.CharField(max_length = 50, blank = True)
	open_date = models.DateField(blank = True, null = True)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']


class Food(models.Model):
	name = models.CharField(max_length = 20)
	price = models.DecimalField(max_digits = 3,decimal_places = 0)
	comment = models.CharField(max_length = 50, blank = True)
	is_spicy = models.BooleanField(default = False)
	restaurant = models.ForeignKey(Restaurant)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['price']

class Comment(models.Model):
	visitor = models.CharField(max_length = 255)
	content = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	date_time = models.DateTimeField()
	restaurant = models.ForeignKey(Restaurant)
	class Meta:
		ordering = ['date_time']
		permissions = (
				('see_comment','Can only see comments'),
				
			)
