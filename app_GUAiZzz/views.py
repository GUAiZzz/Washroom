from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from app_GUAiZzz.models import WashRoom

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    print(request)
    return HttpResponse(c)

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    print(request)
    return HttpResponse(c)

def getdata(request):
    objs = WashRoom.objects.all()
    result = [{"name":i.name, "time":i.time} for i in objs]
    return HttpResponse(result)

def creatdata(request):
    A1 = request
    A2 = request
    A3 = request
    A4 = request

    WashRoom.objects.create(name="A1", time=10)
    WashRoom.objects.create(name="A2", time=10)
    WashRoom.objects.create(name="A3", time=10)
    WashRoom.objects.create(name="A4", time=9)
    WashRoom.objects.bulk_create([0-10])

    WashRoom.objects.get(name=A1)
    WashRoom.objects.get(name=A2)
    WashRoom.objects.get(name=A3)
    WashRoom.objects.get(name=A4)


