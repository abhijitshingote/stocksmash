from django.conf.urls import url
from django.contrib import admin
from .views import IdeaListView,IdeaLDetailView,IdeaCreateView,IdeabyStockView,addcomment

urlpatterns = [
        url(r'^$',IdeaListView.as_view(),name='ideaslist'),
        url(r'^(?P<pk>\d+)/',IdeaLDetailView.as_view(),name='ideadetail'),
        url(r'^create/',IdeaCreateView.as_view(),name='create'),
        url(r'^(?P<ticker>\w+)/',IdeabyStockView.as_view(),name='ideasbystock'),
        url(r'^addcomment/(?P<pk>\d+)/',addcomment,name='addcomment'),



    ]
