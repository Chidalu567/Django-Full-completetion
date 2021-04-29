from django.db import models

class Articles(models.Model): #child class name
    Title=models.CharField(max_length=100); #create a character field
    Content=models.TextField(); #create a text field
    Active=models.BooleanField(default=True); #create a checkbox
