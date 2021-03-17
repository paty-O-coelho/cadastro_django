from django.http import request
from django.shortcuts import render
from .models import Person #importando o model person

def persons_list(request):
    person =  Person.objects.all()
    return render(request, 'person.html', {'persons': person}) 
