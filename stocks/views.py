from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .utils import get_quote
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class IndexView(TemplateView):
	template_name='index.html'

	def get_context_data(self,**kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		stockdict,timestamp=get_quote('BAC,C,SQ,SNAP,AAPL,AMZN,NFLX,NVDA,JPM')
		context['something']='Something is nothing'
		context['stockdict']=stockdict
		context['timestamp']=timestamp
		return context

class SignUpView(CreateView):

	form_class=UserCreationForm
	template_name='registration/signup.html'
	success_url='/login/'