from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class ResultView(ModelViewSet):
    serializer_class = ResultSerializer
    permission_classes=[IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if Result.objects.filter(student__user=user).exists():
            return Result.objects.filter(student__user=user)
        if user.is_superuser:
            return Result.objects.all()
