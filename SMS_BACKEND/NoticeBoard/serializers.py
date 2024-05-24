from rest_framework import serializers
from .models import *
class NoticeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBoard
        fields = "__all__"
        