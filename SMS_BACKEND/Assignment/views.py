from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from authUser.models import *
from courses.models import *
from rest_framework.response import Response
from .permission import *


class AssignmentView(ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes =[IsAuthenticated,AssignmentPermission]

    def get_queryset(self):
        user = self.request.user
        teacher = Teacher.objects.filter(user = user)
        
        if teacher:
            course = Courses.objects.filter(taught_by = user)
            if course:
                return Assignment.objects.filter(created_by=user)

        if Student.objects.filter(student=user) .exists():
            course = MyCourses.objects.filter(student = user)
            batch = Batch.objects.filter(course=course)
            if course:
                assingment = Assignment.objects.filter(batch=batch)
                return assingment
        if user.is_superuser or user.is_staff:
            return Assignment.objects.all()
    

class SubmitAssignmentView(ModelViewSet):
    # queryset=SubmitAssignment.objects.all()
    serializer_class=SubmitAssignmentSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return SubmitAssignment.objects.filter(submitted_by=user)

    def update(self, request, *args, **kwargs):
        return Response({'error':'request not allowed'})