from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember,AuthUser,Activity
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
#回傳Json格式資料使用
from django.http import JsonResponse
#ajax跳過csrf驗證
from django.views.decorators.csrf import csrf_exempt,csrf_protect


current = '' 

def Index(request):
    members = AuthUser.objects.all()
    print(members)
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
def activity(request):
    activities = Activity.objects.all()
    #print(activities)
    return render(request,'Admin/Activity.html',{'activities':activities})

def activityShow(request,name):
    global current
    current = name
    activities = Activity.objects.all()
    activities_list = list(activities)
    for i in activities_list:
        if i.act_name == name:
            resp = [
                {
                    'act_name':i.act_name,
                    'act_date':i.act_date,
                    'act_location':i.location
                }
            ]
    
    return JsonResponse({'showdata':resp})

def activityEdit(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(current)
        print(Activity.objects.filter(act_name = current))
        Activity.objects.filter(act_name = current).update(act_name=request.POST['name'],location=request.POST['location'],act_date=request.POST['date'])
        return redirect('/activity/')

def activityDelete(request,name):
    temp = Activity.objects.filter(act_name = name)
    # temp.delete()
    return redirect('/activity/')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['possword']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             print("sssssss")
#             return redirect('/')
#             # Redirect to a success page.
#     return render(request,'registration/login.html')
            

# Create your views here.
