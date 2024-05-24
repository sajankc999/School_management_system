from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import CoursePermission


class CoursesView(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CousersSerializer
    permission_classes = [CoursePermission]


class MycouserView(ModelViewSet):
    serializer_class = MyCousersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if MyCourses.objects.filter(student__user=user).exists():
            return MyCourses.objects.filter(student__user=user)
        if user.is_superuser or user.is_staff:
            return MyCourses.objects.all()      
