
from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class StudentView(ModelViewSet): 
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    def get_queryset(self):        
        stu= Student.objects.filter(user=self.request.user)
        if stu.exists():
            return stu
        if self.request.user.is_superuser:
            return Student.objects.all()
        

    
class StaffView(ModelViewSet):
    serializer_class = StaffSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):        
        stu= Staff.objects.filter(user=self.request.user)
        if stu.exists():
            return stu
        if self.request.user.is_superuser:
            return Staff.objects.all()

class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes=[IsAuthenticated]
    
    
    def get_serializer_class(self):
        teacher = Teacher.objects.filter(user=self.request.user).exists()
        user = self.request.user
        # raise Exception(teacher)
        if user.is_superuser or teacher:
            return TeacherSerializer
        else:
            return TeacherOtherSerializer
        




    