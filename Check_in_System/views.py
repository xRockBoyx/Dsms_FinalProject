from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember,AuthUser
from django.contrib.auth.models import User
from .forms import *

def Index(request):
    members = AuthUser.objects.all()
    print(members[0].email)
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.name)
            newUser = form.save(commit=False)
            newUser.save()
        
    return render(request,'registeration/register.html')

    

# Create your views here.
