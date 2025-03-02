from django.shortcuts import render
from django.views.generic import ListView
from models import Couses
# Create your views here.


class search(ListView):
    model = Couses
    template_name = 'show'
    context_object_name = 'Serc'
    flieds = ['id','name']