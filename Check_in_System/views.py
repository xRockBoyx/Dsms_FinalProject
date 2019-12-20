from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember,AuthUser,Activity,ActivityAttendList
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#回傳Json格式資料使用
from django.http import JsonResponse
#ajax跳過csrf驗證
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json


current = '' 

def Index(request):
    #superusers = User.objects.all()
    #print(superusers)
    #for i in superusers:
    #    print("user",i)

    #print(members)
   # for i in members:
      #  print(i.user_permissions)
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
        else:
            messages.error(request,"註冊失敗！！！")
        
    return render(request,'registration/register.html',{'form':form})

def activity(request):
    superusers = User.objects.filter(is_superuser=True)
    if  request.user in superusers:
        activities = Activity.objects.all()
        #print(activities)
        return render(request,'Admin/Activity.html',{'activities':activities})
    else:
        return render(request,'User/Activity.html')

@login_required
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


@login_required
def activityEdit(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(current)
        print(Activity.objects.filter(act_name = current))
        Activity.objects.filter(act_name = current).update(act_name=request.POST['name'],location=request.POST['location'],act_date=request.POST['date'])
        return redirect('/activity/')


@login_required
def activityDelete(request,name):
    temp = Activity.objects.filter(act_name = name)
    temp.delete()
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
            


@login_required
def Changeinfo(request):
    
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


@login_required
def AddActivity(request):
    form = AddActivityForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            location = form.cleaned_data.get('location')
            messages.success(request,'新增成功！')
        else:
            messages.error(request,'新增失敗！')
    return render(request,'Admin/AddActivity.html',{'form':form})

def CheckIn(request):
    attendList = ActivityAttendList.objects.all()
    activities = Activity.objects.all()
    
    
    return render(request,'Admin/CheckIn.html',{'activities':activities})


@csrf_exempt
def CheckInObjects(request,name):
    attendList = ActivityAttendList.objects.all()
    activities = Activity.objects.all()
    clubmember = ClubMember.objects.all()

    datetemp =  activities.filter(act_name=name)[0].act_date
    print(datetemp)
    passdata = attendList.filter(act_date=datetemp)


    if request.method == 'POST':
        data = json.loads(request.body)
        id = data["id"]
        actname = data["name"]
        # name = request.POST.get('name')
        # id = request.POST.get('id')
        temp1 = activities.filter(act_name=actname)
        temp = attendList.filter(act_id=id,act_date=temp1.first().act_date)
        print(temp)
        if temp.first().flag == 0:
            temp.update(flag=1)
        else:
            temp.update(flag=0)
    
    return render(request,'Admin/CheckInAction.html',{'activities':activities,'attendlist':passdata,'clubmember':clubmember,'name':name})

def MemberManagement(request):
    clubmembers = ClubMember.objects.all()
    return render(request,'Admin/MemberManagement.html',{'clubmembers':clubmembers})

def CAL (request):
    # AAA = ActivityAttendList.objects.all()
    attendList = ActivityAttendList.objects.all()
    id = request.user.username
    for i in attendList:
        if (i.act_id == id):
            print(i.act_id)
    a = attendList.filter(act_id=id)
    print(a)
    # ActivityAttendList.objects.filter
    return render(request, 'User/club_Attend_list.html')