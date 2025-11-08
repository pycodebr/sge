from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
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


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supplier
    template_name = 'costumer_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('costumer_list')
    permission_required = 'costumers.add_costumer'


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'costumer_detail.html'
    permission_required = 'costumers.view_costumer'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supplier
    template_name = 'costumer_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('costumer_list')
    permission_required = 'costumers.change_costumer'


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'costumer_delete.html'
    success_url = reverse_lazy('costumer_list')
    permission_required = 'costumers.delete_costumer'


class SupplierCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
