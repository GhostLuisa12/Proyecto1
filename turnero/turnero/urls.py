"""turnero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from django.conf.urls.static import static
from django.conf import settings
from apps.turns.views import home, crearTurno, editarTurno, eliminarTurno,cambiarEstado,listTurnsPendientes
from apps.users.views import listUsers, crearUsuario, editarUsuario, eliminarUsuario, costumLogin

urlpatterns = [
    path('API/', include(('apps.API.urls', "API"), namespace="API")),
    path('admin/', admin.site.urls),
    path('',costumLogin, name = 'login'),
    path('saludar/',home),
    path('listTurns/',home,name ='index'),
    path('crear_Turno/',crearTurno,name = 'crear_Turno'),
    path('editar_turno/<int:pk>/',editarTurno, name = 'editar_turno'),
    path('eliminar_turno/<int:pk>/',eliminarTurno.as_view(), name = 'eliminar_turno'),
    path('listUsers/',listUsers, name= 'listUsers' ),
    path('crear_Usuario/',crearUsuario,name = 'crear_Usuario'),
    path('editar_Usuario/<int:pk>',editarUsuario,name = 'editar_Usuario'),
    path('eliminar_Usuario/<int:pk>',eliminarUsuario.as_view(), name = 'eliminar_Usuario'),
    path('cambiarEstado/<int:pk>',cambiarEstado, name = 'cambiarEstado'),
    path('listTurnsPendientes/',listTurnsPendientes,name ='listTurnsPendientes'),
    path('api-auth/', include('rest_framework.urls'))


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)