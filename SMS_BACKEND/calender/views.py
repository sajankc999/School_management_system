from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Calender
from .serializer import *
from .permission import *
from rest_framework.permissions import IsAdminUser

class CalenderView(ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    permission_classes =[CalenderPermission,IsAdminUser]



