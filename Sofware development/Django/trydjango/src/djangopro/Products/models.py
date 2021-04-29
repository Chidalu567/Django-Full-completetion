from django.db import models
from django.urls import reverse

# Create your models here.
#i want to create a back-end that stores the price,descrition and price in database
class Product(models.Model):
    title=models.CharField(max_length=100); #this is a charfield for charater numbering
    description=models.TextField(blank=True,null=True);  #Set a blank and null textfieldd
    website=models.URLField(max_length=100); #create a Url field
    price=models.DecimalField(decimal_places=3,max_digits=100000000); #decimal input of 3dp
    summary=models.TextField(); #this is a text field
    featured=models.BooleanField(default=True);#this is a boolean field
    Email=models.EmailField(max_length=100); #create an email field
    upload=models.FileField(upload_to=r'C:\Users\chidalu craving\Sofware development\Django\trydjango\src\djangopro',max_length=100); #creates an upload field

    def get_absolute_urls(self): #class method definition
        '''Return the url '''
        return reverse('Products:Product',kwargs={'id':self.id}); #return the url id with the name