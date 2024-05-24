from rest_framework import serializers
from .models import *

class CousersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class MyCousersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourses
        fields = "__all__"