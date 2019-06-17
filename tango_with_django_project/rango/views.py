from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    context_dict={'boldmessages':"crunchy,creamy,softy,adi"}
    return render(request,'rango/student_profile.html',context=context_dict)
def doubt(request):
    return render(request,'rango/doubt.html')
def greet(request):
    return HttpResponse(" <a href='/rango/'>Hey </a>how do yo do welcome to django tutorial")