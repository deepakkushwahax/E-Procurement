from django.urls import path
from .views import *
urlpatterns = [
    path('',Register, name='register'),
    path('view_tender/',view_tender,name='view_tender'),
    path('feedback/',feedback,name='feedback'),
]