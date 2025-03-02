from django.contrib import admin
from django.urls import path
from views import ListView,search
from django import views

urlpatterns = [
    path('', search.as_view(),name=search),

]   
