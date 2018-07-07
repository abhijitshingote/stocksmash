from django.shortcuts import render,redirect
from django.views.generic import (ListView,DetailView,
	CreateView,UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Idea,Comment
from stocks.models import Stock
from .forms import IdeaForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

class IdeaListView(ListView):

	model=Idea
	paginate_by=25
	ordering=['-created']

	# def get_context_data(self,**kwargs):
	# 	context=super(IdeaListView,self).get_context_data(**kwargs)
	# 	context['idea']=context
	# 	return context

class IdeaLDetailView(DetailView):

	model=Idea

	def get_context_data(self,**kwargs):
		context=super(IdeaLDetailView,self).get_context_data(**kwargs)
		context['idea']=self.object
		i=self.object
		comments=i.comment_set.all().order_by('-created')
		context['comments']=comments
		return context

	def post(self,request,*args,**kwargs):

		comment=request.POST.get('comment')
		Comment.objects.create(comment_text=comment,user=request.user,
			idea=Idea.objects.get(pk=self.kwargs.get('pk')))
		return HttpResponseRedirect(reverse('ideas:ideadetail',args=[self.kwargs.get('pk')]))

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

def addcomment(request,pk):
	comment=request.POST.get('comment')
	Comment.objects.create(comment_text=comment,user=request.user,
			idea=Idea.objects.get(pk=pk)
		)
	# return redirect('some-view-name', foo='bar')self
	return HttpResponseRedirect(reverse('ideas:ideadetail', args=[pk]))



