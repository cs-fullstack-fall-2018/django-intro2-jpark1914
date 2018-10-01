from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request, name):
    return HttpResponse(("Hello", name))

def times2(request, number):
    return HttpResponse(("The product times 2 is ", int(number)*2))

def addition(request, sum):
    for x in range(0,sum):
        sum += x
        print(x)
        print(sum)
    return HttpResponse(int(sum))
