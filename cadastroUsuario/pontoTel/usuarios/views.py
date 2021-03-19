from django.http import request
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required  #decoreito para a segurança da aplicação
from .models import Person #importando o model person
from .forms import PersonForm

#get_obj...404 tenta acessar o objeto que o usuario esta acessando
@login_required
def persons_list(request):
    person =  Person.objects.all()
    return render(request, 'person.html', {'persons': person}) 

@login_required
def persons_new(request):
    form =  PersonForm(request.POST or None, request.FILES or None)
    #validar e salvar os dados
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_forms.html',{'form': form})

@login_required
def persons_update(request, id):
    person =  get_object_or_404(Person, pk=id)
    form =  PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_forms.html', {'form': form})
    
@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})

















