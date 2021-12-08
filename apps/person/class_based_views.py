from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Person
from .forms import PersonForm


class PersonList(ListView):
  model = Person

  def get_queryset(self):
    return self.model.objects.all()[:]


class PersonCreate(CreateView):
  model = Person
  form_class = PersonForm
  #template_name = 'add_person.html'
  success_url = reverse_lazy('homepage')


class PersonUpdate(UpdateView):
  model = Person
  form_class = PersonForm
  #template_name = 'add_person.html'
  success_url = reverse_lazy('homepage')


class PersonDelete(DeleteView):
  model = Person
  template_name = 'confirm_delete.html'
  success_url = reverse_lazy('homepage')