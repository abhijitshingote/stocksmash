from django.db import models
from django.shortcuts import reverse
from django.conf import settings
# Create your models here.

User=settings.AUTH_USER_MODEL

class Idea(models.Model):

	tickersymbol=models.ForeignKey('stocks.Stock',on_delete=models.CASCADE)
	long_short=models.CharField(max_length=5,blank=False,choices=(('LONG','LONG'),('SHORT','SHORT')))
	buyprice=models.DecimalField(decimal_places=2,max_digits=9)
	buytimestamp=models.DateField(auto_now=True)
	targetprice=models.DecimalField(decimal_places=2,max_digits=9)
	tradeenddate=models.DateField()
	stoplossprice=models.DecimalField(decimal_places=2,max_digits=9)
	shortthesis=models.TextField(max_length=100)
	longthesis=models.TextField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	created=models.DateField(auto_now_add=True)
	updated=models.DateField(auto_now=True)


	def __str__(self):
		return str(self.tickersymbol)+str(self.buytimestamp)

	def get_absolute_url(self):
		return reverse('ideas:ideadetail',kwargs={'pk': self.pk})

class Comment(models.Model):
	comment_text=models.TextField()
	user=models.ForeignKey(User)
	idea=models.ForeignKey(Idea)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.comment_text[:20]