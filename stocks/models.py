from django.db import models

# Create your models here.
class Stock(models.Model):

	tickersymbol=models.CharField(max_length=6)
	created=models.DateField(auto_now_add=True)
	updated=models.DateField(auto_now=True)


	def __str__(self):
		return self.tickersymbol