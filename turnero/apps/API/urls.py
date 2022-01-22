import apps.API.views as apiView
from apps.API.views import turnsListApi , userView,send_email,userCheckView
from django.urls import path
from django.urls import include, re_path



urlpatterns = [

    path('turnsListApi/', apiView.turnsListApi.as_view(), name= 'turnsListApi'),
    re_path(r'userCheckView/', apiView.userCheckView.as_view(), name = 'userCheckView'),

]