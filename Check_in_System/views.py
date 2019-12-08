from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClubMember

def Index(request):
    members = ClubMember.objects.all()
    print(members)
    return render(request,'index.html')

# Create your views here.
