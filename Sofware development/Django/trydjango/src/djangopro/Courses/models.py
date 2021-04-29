from django.db import models

class Course(models.Model):
    Title=models.CharField(max_length=100); #create a character field
    Content=models.TextField(); #create a textfield
    Date=models.DateTimeField(auto_now_add=True); #create a date field
    View=models.IntegerField(default=0); #create an interger field
    Active=models.BooleanField(default=True); #create a boolean field or a check_box

