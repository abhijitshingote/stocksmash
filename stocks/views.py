from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .utils import get_quote,get_stockdata
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class IndexView(TemplateView):
	template_name='index.html'

	def get_context_data(self,**kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		stocklist='SABR,DIN,MA,TSLA,SRPT,WIX,AAPL,C,CIX,JPM,NVDA,GOOG,NFLX,AMZN,SQ,MS,GS'
		stockdict,timestamp=get_stockdata(stocklist,'50','14')
		
		context['stockdict']=stockdict
		context['timestamp']=timestamp
		return context

class SignUpView(CreateView):

	form_class=UserCreationForm
	template_name='registration/signup.html'
	success_url='/login/'