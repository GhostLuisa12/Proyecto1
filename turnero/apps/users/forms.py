from django import forms
from apps.users.models import persona

class usuarioform(forms.ModelForm):
    class Meta:
        model = persona
        fields = [
            'name',
            'lastname',
            'phone',
            'idNumber',
            'staff',
            'picture',
            #'password2',
        ]
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'phone': 'Celular',
            'idNumber': 'Numero de identificacion',
            'staff':'Funcionario',
            'picture':'foto',
            # 'group': 'Grupo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Nombre'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Apellidos'}),
            'phone': forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Telefono'}),
            'idNumber': forms.TextInput(attrs={ 'class': 'form-control ','placeholder': 'Numero de identificacion'}),
            'staff': forms.Select(attrs={ 'class': 'form-control '}), 
            'picture': forms.FileInput(attrs={ 'class': 'form-control '}), 

        }