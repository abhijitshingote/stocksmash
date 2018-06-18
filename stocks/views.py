from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import get_quote

# Create your views here.
class IndexView(TemplateView):
	template_name='index.html'

	def get_context_data(self,**kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		stockdict,timestamp=get_quote('BAC,C,SQ,SNAP,AAPL')
		context['something']='Something is nothing'
		context['stockdict']=stockdict
		context['timestamp']=timestamp
		return context