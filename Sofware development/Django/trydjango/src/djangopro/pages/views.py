from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


# Create your views here
def home_view(request,*args,**kwargs): #function definition
    print(request.user); #show the user when a request is made
    return render(request,'Main.html',{}); #render value for a request
    #return HttpResponse('<h1>Welcome To My Custom Page</h1>'); #thisis a django function

def about_view(request,*args,**kwargs): #fuction definition
    print(request.user); #shows the user when a request of about is made
    my_context={
        "Head":'This is a header1 Tag',
        "Name":'Chidalu Fortune',
        "Age":14,
        "Datas":['ss3','python','Love GOD'],
        "my_html":'<h2>This is a header2 tag</h2>'
    }; #python dictionary definition
    return render(request,'about.html',my_context); #return a template to the user requesting
    #return HttpResponse('<h1>About Page</h1>'); #django function

def contact_view(request,*args,**kwargs): #function definitioin
    print(request.user); #shows the user when a request of contactis made
    return render(request,'contact.html',{}); #return a template to the user
    #return HttpResponse('<h1>Contact Page</h1>'); #response to webpage

def store_view(request,*args,**kwargs): #class method definition
    return render(request,'store/cart.html')

def payment_view(request,*args,**kwargs): #class method definition
    paypal_dict={
        'business':settings.PAYPAL_RECEIVER_EMAIL,
        'currency':'USD',
        'amount':30.2,
        'item_name':'PlayStation',
        'invoice':2,
        'notify_url':'http://{}{}'.format('127.0.0.1:8000',reverse('paypal-ipn')),
        'return_url':'http://{}{}'.format('127.0.0.1:8000',reverse(done_view)),
        'cancel_url':'http://{}{}'.format('127.0.0.1:8000',reverse(cancel_view))
    }; #python dictionary definition\
    form=PayPalPaymentsForm(initial=paypal_dict,button_type='subscribe'); #create paypal form
    return render(request,'store/process-payment.html',{'form':form});

@csrf_exempt
def done_view(request,*args,**kwargs): #class method definition
    return render(request,'store/payment-done.html');
@csrf_exempt
def cancel_view(request,*args,**kwargs): #class method definition
    return render(request,'store/payment-cancel.html'); #return this tempate for this request





