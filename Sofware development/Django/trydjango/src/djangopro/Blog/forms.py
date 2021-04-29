from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm): #child class name
    Title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'placeholder':'Enter Title'
    })); #create a character field with a maximum length of 100
    Content=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Enter Contents Here'
    })); #create a character field in form of a textarea
    Active=forms.BooleanField(); #create a checkbox
    class Meta:
        model=Article
        fields=[
            'Title',
            'Content',
            'Active'
        ]

