from django.shortcuts import render
from apps.turns.models import turnos
from apps.turns.serializers import turnsSerializer
from apps.users.serializers import userSerializer
from rest_framework.response import Response
from rest_framework import status



from rest_framework.decorators import api_view,permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated,AllowAny 
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
    ListAPIView,
    GenericAPIView,
    ListCreateAPIView,
)
from apps.users.models import persona

# Create your views here.
@permission_classes((AllowAny, ))
class turnsListApi(ListAPIView):
    queryset = turnos.objects.all()
    serializer_class = turnsSerializer

@permission_classes((AllowAny, ))
class userView(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = userSerializer

@permission_classes((AllowAny, ))
class userCheckView(APIView):

    def post(self, request):
        print("entra en la nueva API")
        print("request.data::",request.data)
        refuse = request.data['refuse']

        content = {
            'details':
            'Reason refuce created.'
        }
        return Response(content)


def send_email(request):
    try:
        print("request",request.POST)
        receiver = request.POST.get('receiver')
        title = request.POST.get('title')
        body = request.POST.get('body')
        sender = 'leonardo.novoa@eurekadms.com'
        url = request.POST.get('url')
       
        content = {'Detail': 'correo enviado'}
        return Response(content, status=status.HTTP_200_OK)
    except Exception as e:
        content = {'error': e}
        return Response (content,status=status.HTTP_400_BAD_REQUEST)