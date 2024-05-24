from rest_framework import serializers
from .models import *

class SuggestionBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionBox
        fields = ['id','created_at','title','content']
