from django import forms
from gestao_app.models import Edificio, Apartamento

class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento
        fields = ['ap_name', 'ap_status', 'edificio_id', 'valor_aluguel', 'locatario_nome', 'locatario_contato']
        widgets = { 'ap_name': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'ap_status': forms.IntergerInput(attrs={ 'class': 'form-control' }),
                    'edificio_id': forms.IntergerInput(attrs={ 'class': 'form-control' }),
                    'valor_aluguel': forms.FloatInput(attrs={'class': 'form-control'}),
                    'locatario_nome': forms.TextInput(attrs={'class': 'form-control'}),
                    'locatario_contato': forms.TextInput(attrs={'class': 'form-control'}),
      }

class EdificioForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ['edificio_name']
        widgets = { 'edificio_name': forms.TextInput(attrs={ 'class': 'form-control' }),
      }