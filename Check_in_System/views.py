from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember,AuthUser

def Index(request):
    members = AuthUser.objects.all()
    print(members[0].email)
    return render(request,'index.html')

# Create your views here.
