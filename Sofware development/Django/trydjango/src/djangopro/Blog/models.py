from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model): # child class name
        Title=models.CharField(max_length=100); #create a character field with a max_length of 100
        Content=models.TextField(); #create a text field
        Active=models.BooleanField(default=True); #create a checkbox

        def get_absolute_url(self):
            return reverse('Blog:Detail_view',kwargs={'my_id':self.id}); #return the url name and id