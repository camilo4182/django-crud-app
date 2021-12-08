from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def homepage(request):
  people = Person.objects.all() # Returns all instances of Person class
  print(people)
  context = {
    'people': people,
  }
  return render(request, 'index.html', context)

def add_person(request):
  if request.method == 'GET':
    form = PersonForm()
    context = {
      'form': form
    }
  elif request.method == 'POST':
    form = PersonForm(request.POST)
    print(form)
    context = {
      'form': form
    }
    if form.is_valid():
      form.save()
      return redirect('homepage')
  return render(request, 'add_person.html', context)

def edit_person(request, id):
  person = Person.objects.get(id = id)
  if request.method == 'GET':
    form = PersonForm(instance = person)
    context = {
      'form': form
    }
  elif request.method == 'POST':
    form = PersonForm(request.POST, instance = person)
    context = {
      'form': form
    }
    if form.is_valid():
      form.save()
      return redirect('homepage')
  return render(request, 'add_person.html', context)
