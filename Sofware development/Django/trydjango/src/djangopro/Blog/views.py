from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Article
from .forms import ArticleModelForm
from django.urls import reverse

# Create your views here.
class ArticleCreateView(CreateView): #child class name
    template_name='articles/create_list.html';
    form_class=ArticleModelForm; #this is the form class
    queryset=Article.objects.all(); #get all the objects in the database

    #def form_valid(self,form):
     #   print(form.cleaned_data); #oprint the valu=e in the form
      #  return super().form_valid(form);

class ArticleListView(ListView): #child class name
    template_name='articles/article_list.html';
    queryset=Article.objects.all(); #get all the objects in the database

class ArticleDetailView(DetailView): #child class name
    template_name='articles/detail_list.html'; #the template_name for my class based view
    queryset = Article.objects.all(); #get allt the objects in the database

    def get_object(self):#built_in function for class based vies
        my_id=self.kwargs.get('my_id');
        return get_object_or_404(Article,id=my_id)

class ArticleUpdateView(UpdateView): #child class name
    template_name='articles/create_list.html';
    form_class=ArticleModelForm; #this is the form class
    queryset=Article.objects.all(); #get all the objects in the database

    def get_object(self): #builtin class method
        my_id=self.kwargs.get('my_id'); #get my_id in the url
        return get_object_or_404(Article,id=my_id); #get object with id from the database

class ArticleDeleteView(DeleteView): #child class name
    template_name='articles/delete_list.html'; #This is the template name path
    queryset=Article.objects.all(); #get all the objects in the database

    def get_object(self): #class method definition
        my_id=self.kwargs.get('selected_id'); #get the id in te url
        return get_object_or_404(Article,id=my_id); #get the object in the database with id of my_id

    def get_success_url(self): #get the success url
        return reverse('Blog:Listview');  #return the url to go to when object is deleted
    