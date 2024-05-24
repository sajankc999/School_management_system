from rest_framework import serializers
from .models import *

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = "__all__"