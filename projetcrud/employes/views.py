from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from .models import Employe
from .forms import Employeform
from django.urls import reverse_lazy

class EmployeListView(ListView):
    model = Employe
    template_name = 'index.html'
    context_object_name = 'employes'

# class pour l'ajout des employés
class EmployeAjout(CreateView):

    model = Employe
    form_class = Employeform
    template_name = 'index.html'
    success_url = reverse_lazy('employe_list')
    

#class pour la modification
class EmployEdit(UpdateView):

    model = Employe
    form_class = Employeform
    template_name = 'index.html'
    success_url = reverse_lazy('employe_list')