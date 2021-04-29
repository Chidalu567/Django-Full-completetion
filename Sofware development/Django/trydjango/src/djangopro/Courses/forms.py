from django import forms
from .models import Course

class CourseForm(forms.ModelForm): #class name definition
    Title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter Title Here'})); #create a charcter field
    class Meta:
        model=Course; #The model name
        fields=['Title']; #python list definition

    def clean_Title(self): #form validation method
        title=self.cleaned_data.get('Title'); #get the value of the cleaned_data of Title keyword in the dictionary
        if title.lower() == 'love':
            raise forms.ValidationError('This is not a valid title');
        return title

