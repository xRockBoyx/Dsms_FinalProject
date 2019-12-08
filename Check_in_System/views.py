from django.shortcuts import render,redirect
from django.http import HttpResponse

def Index(request):
    return render(request,'index.html')

# Create your views here.
