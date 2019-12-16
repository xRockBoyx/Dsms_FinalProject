from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember,AuthUser
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

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
            messages.success(request,"註冊成功！！！")
            return redirect('/')
        
    return render(request,'registration/register.html',{'form':form})

#def login(request):
    
#    if request.method == 'POST':
        #print(request.POST)
        #print(request.POST[])
#        username = request.POST['username']
#        password = request.POST['password']
        
        
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            print("sssssss")
#            return redirect('/')
            # Redirect to a success page.
#    return render(request,'registration/login.html')

def Changeinfo(request):
    #for e in AuthUser.objects.all():
        #print(e.username)
    #print(request.user)
    #form = AuthUser.objects.filter(username=request.user.username)
    
    
    for e in AuthUser.objects.all():
        #print(e.username,request.user)
        if e.username == request.user.username:
            form = e
            break
    print(form.phone)
    #print(form.username)

    if request.method == 'POST':
        print(request.user.username)
        print(request.POST)
        messages.success(request,"更改成功！！！")
        AuthUser.objects.filter(username = request.user.username).update(email = request.POST['email'], phone = request.POST['phone'], deparement=request.POST['deparement'])
        return redirect('/')
    
    return render(request,'User/Changeinfo.html',{'form':form})

# Create your views here.
