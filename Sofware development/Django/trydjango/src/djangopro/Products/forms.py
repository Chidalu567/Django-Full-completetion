from django import forms
from .models import Product

class RawProductForm(forms.ModelForm): #a pure django form
    title=forms.CharField(max_length=100,required=False,widget=forms.TextInput(
        attrs={
            'placeholder':'Write Title'
        }
    )
                          ); #create a character field with a max_length of 100
    description=forms.CharField(max_length=1000,required=True,widget=forms.Textarea(
        attrs={
            'placeholder':'Enter Description',
            'rows':5,'cols':100,
            'class':'description_class',
            'id':'description_id'
        }
    )
                                ); #create a character field with a max_length of 1000
    Email=forms.EmailField() #create an email form field
    price=forms.DecimalField(decimal_places=2,max_digits=100000,required=True,initial=199.99); #create a decimal field

    class Meta:
        model=Product; #name of the model
        fields=['title','description','price','Email']; #The fields we want to show in our template

    def clean_title(self,*args,**kwargs): # class method definition
        title=self.cleaned_data.get('title'); #get the value of the key 'title'
        if not 'Pacific' in title:
            raise forms.ValidationError('You forgot to put Pacific')
        if not 'Gold' in title:
            raise forms.ValidationError('You Forgot to put Gold');
        return title; #return title

    def clean_email(self,*args,**kwargs): #class method definition
        email=self.cleaned_data.get('Email'); #get the value of key 'Email'
        if not email.endswith('edu')| email.endswith('org'):
            raise forms.ValidationError('Please enter a valid email address')
        return email