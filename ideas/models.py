from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Idea(models.Model):

	tickersymbol=models.ForeignKey('stocks.Stock',on_delete=models.CASCADE)
	buyprice=models.DecimalField(decimal_places=2,max_digits=9)
	buytimestamp=models.DateField(auto_now=True)
	targetprice=models.DecimalField(decimal_places=2,max_digits=9)
	tradeenddate=models.DateField()
	stoplossprice=models.DecimalField(decimal_places=2,max_digits=9)
	shortthesis=models.TextField(max_length=100)
	longthesis=models.TextField()
	created=models.DateField(auto_now_add=True)
	updated=models.DateField(auto_now=True)


	def __str__(self):
		return str(self.tickersymbol)+str(self.buytimestamp)

	def get_absolute_url(self):
		return reverse('ideas:ideadetail',kwargs={'pk': self.pk})