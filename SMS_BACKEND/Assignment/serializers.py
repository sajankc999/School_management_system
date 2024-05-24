from rest_framework import serializers
from .models import *

class AssignmentSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model= Assignment
        fields = "__all__"

class SubmitAssignmentSerializer(serializers.ModelSerializer):
    submitted_by = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model= SubmitAssignment
        fields = "__all__"


class CheckAssignmentSerializer(serializers.ModelSerializer):
    checked_by = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model= CheckAssignment
        fields = "__all__"