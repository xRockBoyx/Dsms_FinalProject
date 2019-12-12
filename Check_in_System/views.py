from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember,AuthUser
from .forms import *

def Index(request):
    members = AuthUser.objects.all()
    print(members[0].email)
    return render(request,'index.html')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        #AuthUser.objects.create(username=data['name'],deparement=data['deparement'],email=data['email'],phone=['phone'],password=['password'],is_superuser=0,is_staff=1,is_active=1)
        # print(form)
        if form.is_valid():
        #    print(form)
        #    newUser = form.save(commit=False)
             form.save()
             redirect('index.html')
        else:
            print(form.errors)
        
    return render(request,'registeration/register.html',{'form':form})

    

# Create your views here.
