from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class SuggestionBoxView(ModelViewSet):
    serializer_class = SuggestionBoxSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if SuggestionBox.objects.filter(created_by=user).exists():
            return SuggestionBox.objects.filter(created_by=user)
        if user.is_superuser or user.is_staff:
            return SuggestionBox.objects.all()
