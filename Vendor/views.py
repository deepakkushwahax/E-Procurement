from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import random


# Create your views here.

def Register(request):
    template=loader.get_template('Register.html')
    return HttpResponse(template.render())

def view_tender(request):
    return render(request,'view_tender.html')

def feedback(request):
    return render(request,'feedback.html')
