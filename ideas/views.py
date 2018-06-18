from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Idea
from .forms import IdeaForm
# Create your views here.

class IdeaListView(ListView):

	model=Idea

class IdeaLDetailView(DetailView):

	model=Idea

	def get_context_data(self,**kwargs):
		context=super(IdeaLDetailView,self).get_context_data(**kwargs)
		context['idea']=self.object
		return context

class IdeaCreateView(CreateView):
	form_class=IdeaForm
	model=Idea



