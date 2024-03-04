from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import Companies
from django.contrib.auth.mixins import LoginRequiredMixin


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'

class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['name', 'website', 'company_type']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')

class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'website', 'company_type']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')

@login_required
def delete_location(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:lista_companii')

@login_required()
def activate_location(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:lista_companii')
