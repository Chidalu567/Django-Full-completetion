from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles

# Create your views here.
class ArticlesListView(ListView):
    template_name ='articles/articles_list.html';
    queryset=Articles.objects.all(); #get all the ibject in the database

