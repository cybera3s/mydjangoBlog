from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse("hi sajad i am fucking programmer! ")
    return render(request , 'about.html')

def home(request):
    # return HttpResponse("fuck this is home")
    return render(request , 'Home.html')
