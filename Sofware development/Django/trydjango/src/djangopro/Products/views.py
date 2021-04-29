from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import RawProductForm


# Create your views here.
def product_view(request,*args,**kwargs): #function definition
    #obj1=Product.objects.get(id=1); #get object with id of 1
    Queryset=Product.objects.all(); #gets all the ibject in the database
    context={
        'object_list':Queryset
    }
    return render(request,'product/home.html',context); #Return a template for a request made

def product_create_view(request,*args,**kwargs): #function definition
    #obj1=Product.objects.get(id=14); #get object with id of 14
    form=RawProductForm(request.POST or None); #create an instance with an initial of the 14th object
    if form.is_valid(): #if form is valid
        form.save(); #save value in database if validation is passed
        form=RawProductForm(); #create an instance
    context={
        'Form':form
    }
    return render(request,'product/create.html',context); #render this template for a request

def dynamic_lookup_view(request,my_id): #function definition
    obj=get_object_or_404(Product,id=my_id); #get object with id of my_id or page not found(404)
    context={
        'object':obj
    }; #python dictionary definition
    return render(request,'product/dynamic_template.html',context); #render the template for a request

def delete_view(request,my_id): #function definition
    obj=get_object_or_404(Product,id=my_id); #get object with id of my_id or error 404(page not found)
    if request.method == "POST": #if the request of the form is post
        '''Confirming a delete'''
        obj.delete()# #delete the object from the database
        return redirect('../../'); #redirect them back two steps in the url
    context={
        'object':obj
    }; #python dictionary definition
    return render(request,'product/delete.html',context); #Render the template for a request