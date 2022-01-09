from django.http.response import HttpResponse
from django.shortcuts import render
from .models import main,educations,certifications,skills,achievements,hobbies
# Create your views here.
def index(request):
    
    dest=main.objects.all()
    return render(request,'index.html',{'data':dest})

def education(request):
    dest1=educations.objects.all()
    return render(request,'edu.html',{"data":dest1})

def certification(request):
    dest2=certifications.objects.all()
    return render(request,'cert.html',{'data':dest2})

def skill(request):
    dest3=skills.objects.all()
    return render(request,'skill.html',{'data':dest3})

def achievement(request):
    dest4=achievements.objects.all()
    return render(request,'achieve.html',{'data':dest4})

def hobbie(request):
    dest5=hobbies.objects.all()
    return render(request,'hobbie.html',{'data':dest5})