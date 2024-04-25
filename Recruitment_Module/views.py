from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import random

# Create your views here.

def Recuitment_Module(request):
    template=loader.get_template('Recuitment.html')
    return HttpResponse(template.render())

