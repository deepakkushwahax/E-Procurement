from django.urls import path
from .views import *


urlpatterns = [
    path('',Recuitment_Module, name='Recuitment_Module'),
    path('Jobs_details/',Job_details,name='Job_details.html')
]
