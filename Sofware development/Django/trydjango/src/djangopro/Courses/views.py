from django.shortcuts import render,get_object_or_404,redirect
from .models import Course
from django.views import View
from .forms import CourseForm

class CourseView(View): #child class name
    template_name='Course/About.html'; #defualt template name
    def get(self,request,id=None,*args,**kwargs):
        context={}; #python dictionary definition
        if id is not None:
            id_obj=get_object_or_404(Course,id=id); #get the object with 'id' else give 404 error(page not found)
            context['object']=id_obj;
        else:
            obj=Course.objects.all(); #get all objects value in database
            context['object']=obj;


        return render(request,self.template_name,context); #return the template for a request

class CourseListView(View):
    template_name='Course/list.html'; #the template name
    queryset=Course.objects.all(); #this is a queryset

    def get_queryset(self): #class method
        return self.queryset;

    def get(self,request,*args,**kwargs): #built-in class method definition
        context={'object_list':self.get_queryset()}; #python dictionary definiton
        return render(request,self.template_name,context); #render a template for a query

class CourseCreateView(View):
    template_name='Course/create.html'; #the template name
    queryset=Course.objects.all(); #this is a queryset

    def get(self,request,*args,**kwargs): #built-in class method definition
        Form=CourseForm(request.GET or None); #create a get form method
        context={'form':Form}; #python dictionary definiton
        return render(request,self.template_name,context); #render a template for a query

    def post(self,request,*args,**kwargs): #built-in class method definition
        #A post method allows us to save value in the database
        Form=CourseForm(request.POST or None); #create a post method form
        if Form.is_valid():
            Form.save(); #save value in the database
            Form=CourseForm(); #create a get method form leaving it emoty
        context={'form':Form}; #python dictionary definiton
        return render(request,self.template_name,context); #render a template for a query

class CourseUpdateView(View): #child class name
    template_name='Course/update.html'; #template name

    def get_object(self): #get object finction
        my_id=self.kwargs.get('id'); #get the id in the url
        obj=None; #None
        if my_id is not None:
            obj=get_object_or_404(Course,id=my_id); #get the object in the database or error page not found(404)
        return obj

    def get(self,request,id=None,*args,**kwargs): #class method definition
        obj=self.get_object(); #get the object
        context={}; #python dictionary declration

        if obj is not None:
            form = CourseForm(request.GET or None,instance=obj);  # create a get method
            context['object']=obj;
            context['form']=form;
        return render(request,self.template_name,context); #return a template for the query

    def post(self,request,id=None,*args,**kwargs): #class method definition
        obj=self.get_object();
        context={}; #python dictionary declration
        if obj is not None:
            form = CourseForm(request.POST or None,instance=obj);  # create a post method form to save value in database
            context['object']=obj;
            context['form']=form;
        if form.is_valid():
            form.save() #save udate to database
            form=CourseForm();
        return render(request,self.template_name,context); #return a template for the query

class CourseDeleteView(View): #child class definition
    template_name='Course/delete.html'; #template name

    def get_object(self): #class method definition
        id=self.kwargs.get('id'); #get the id from the url passed
        obj=None
        if id is not None:
            obj=get_object_or_404(Course,id=id); #get the object from the model with id of  id
        return obj; #return the object

    def get(self,request,id=None,*args,**kwargs):
        obj=self.get_object(); #class method call
        context={}; #python dictionary declaration
        if obj is not None:
            context['object']=obj;
        return render(request,self.template_name,context);

    def post(self,request,*args,**kwargs): #class method definition
        obj=self.get_object(); #class method call
        context={}; #python dictionary definitioin
        if obj is not None:
            context['object']=obj
        if request.method =='POST':
            obj.delete(); #delete object
            context['object']=None;
            return redirect('/Courses/'); #redirect user when object is deleted
        return render(request,self.template_name,context);
