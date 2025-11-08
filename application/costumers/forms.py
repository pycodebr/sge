from django import forms
from . import models


class CostumerForm(forms.ModelForm):

    class Meta:
        model = models.Costumer
        fields = ['name', 'mail', 'phone', 'document_id', 'address', 'city' , 'state' , 'zip_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'document_id': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),            
        }
        labels = {
            'name': 'Nome',
            'mail': 'E-mail',
            'phone': 'Telefone',
            'document_id': 'CPF/CNPJ',
            'address': 'Endereço',
            'city': 'Cidade',
            'state': 'Estado',
            'zip_code': 'CEP',
        }
