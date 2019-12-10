from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember,AuthUser
from django.contrib.auth.models import User
from .forms import *

def Index(request):
    members = AuthUser.objects.all()
    print(members[0].email)
    return render(request,'index.html')

def SignUp(request):
    if request.method == 'POST':
        form = RegisterForm(request.post)
        print()
    else :
        return render(request,'SignUp.html')

    

# Create your views here.
