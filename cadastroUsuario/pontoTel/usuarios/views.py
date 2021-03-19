from django.http import request
from django.shortcuts import render, redirect
from .models import Person #importando o model person
from .forms import PersonForm

def persons_list(request):
    person =  Person.objects.all()
    return render(request, 'person.html', {'persons': person}) 

def persons_new(request):
    form =  PersonForm(request.POST, request.FILES, None)
    #validar e salvar os dados
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_forms.html',{'form': form})