
from rest_framework.serializers import ModelSerializer
from apps.turns.models import turnos
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers


class turnsSerializer(ModelSerializer):
  #  studies = studiesSerializer(many = True)
    class Meta:
        model = turnos
        #fields = ('name', 'pk', 'icon')
        fields = ('__all__')