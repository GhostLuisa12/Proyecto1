from pyexpat import model
from django.db import models

from apps.users.models import persona

# Create your models here.

class estados(models.Model):
    name =models.CharField(max_length=100)
    def __str__(self):
        return self.name

class turnos(models.Model):
    cod =models.CharField(max_length=6)
    numCod =models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state =models.ForeignKey(estados,related_name='states', null=True, on_delete=models.SET_NULL)
    user =models.ForeignKey(persona,related_name='user', null=True, on_delete=models.SET_NULL)
    userStaff =models.ForeignKey(persona,related_name='userStaff', null=True, on_delete=models.SET_NULL)
    def __str__(self):
         return "%s %s" % (self.cod, self.numCod)