from django import forms
from apps.turns.models import turnos

class turnosform(forms.ModelForm):
    class Meta:
        model = turnos
        fields = [
            'cod',
            'numCod',
            'state',
            'user',
            'userStaff',
                    
        ]

        labels = {
            'cod': 'Código',
            'numCod': 'Número Código',
            'state': 'Estado',
            'user': 'Usuario',
            'userStaff':'Funcionario',
            
         
        }

        widgets = {
            'cod': forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Código'}),
            'numCod': forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Número Código'}),
            'state': forms.Select(attrs={'class': 'form-control ','placeholder': 'Estado'}),
            'user': forms.Select(attrs={ 'class': 'form-control ','placeholder': 'Usuario'}),
            'userStaff': forms.Select(attrs={ 'class': 'form-control', 'placeholder':'Funcionario'}), 
    
        }
