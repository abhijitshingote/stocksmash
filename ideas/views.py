from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
	CreateView,UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Idea
from stocks.models import Stock
from .forms import IdeaForm
from django.shortcuts import get_object_or_404
# Create your views here.

class IdeaListView(ListView):

	model=Idea

class IdeaLDetailView(DetailView):

	model=Idea

	def get_context_data(self,**kwargs):
		context=super(IdeaLDetailView,self).get_context_data(**kwargs)
		context['idea']=self.object
		return context

class IdeaCreateView(LoginRequiredMixin,CreateView):
	form_class=IdeaForm
	model=Idea
	login_url='/login/'

	def form_valid(self,form):
		form.instance.user=self.request.user
		return super(IdeaCreateView,self).form_valid(form)

	# def get_form_kwargs(self):
	# 	kwargs=super(IdeaCreateView,self).get_form_kwargs()
	# 	kwargs['user']=self.request.user
	# 	return kwargs

class IdeabyStockView(ListView):

	def get_queryset(self):
		ticker=get_object_or_404(Stock,tickersymbol=self.kwargs['ticker'])
		return Idea.objects.filter(tickersymbol=ticker)


