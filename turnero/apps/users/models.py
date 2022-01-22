from pyexpat import model
from django.db import models

class staffCheck(models.Model):
    value =models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.value

# Create your models here.
class persona(models.Model):
    name =models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=120,null=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    idNumber = models.CharField(max_length=100,null=True)
    staff =models.ForeignKey(staffCheck,related_name='stafCheck', null=True, on_delete=models.SET_NULL)
    picture = models.ImageField(upload_to ='pictures/',null=True)
    def __str__(self):
        return self.name


