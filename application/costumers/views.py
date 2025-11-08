from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers
from django.http import HttpResponse
import csv


class CostumerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Costumer
    template_name = 'costumer_list.html'
    context_object_name = 'costumers'
    paginate_by = 10
    permission_required = 'costumers.view_costumer'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CostumerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Costumer
    template_name = 'costumer_create.html'
    form_class = forms.CostumerForm
    success_url = reverse_lazy('costumer_list')
    permission_required = 'costumers.add_costumer'


class CostumerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Costumer
    template_name = 'costumer_detail.html'
    permission_required = 'costumers.view_costumer'


class CostumerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Costumer
    template_name = 'costumer_update.html'
    form_class = forms.CostumerForm
    success_url = reverse_lazy('costumer_list')
    permission_required = 'costumers.change_costumer'


class CostumerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Costumer
    template_name = 'costumer_delete.html'
    success_url = reverse_lazy('costumer_list')
    permission_required = 'costumers.delete_costumer'


class CostumerCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Costumer.objects.all()
    serializer_class = serializers.CostumerSerializer


class CostumerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Costumer.objects.all()
    serializer_class = serializers.CostumerSerializer

def costumers_export(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="clientes.csv"'
    writer = csv.writer(response)
    writer.writerow(["Nome", "E-mail", "Telefone", "CPF/CNPJ", "Endereço", "Cidade", "Estado", "CEP", "Data de Criação"])

    for c in models.Costumer.objects.all():
        writer.writerow([c.name, c.mail, c.phone, c.document_id, c.address, c.city, c.state, c.zip_code, c.created_at])

    return response
