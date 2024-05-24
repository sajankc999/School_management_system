from .views import *
from django.urls import path
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('students',StudentView,basename='student')
router.register('teacher',TeacherView,basename='teacher')
router.register('staff',StaffView,basename='staff')

urlpatterns = [
    
]+router.urls

