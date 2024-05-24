from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('submitassignment',SubmitAssignmentView,basename='submit assigment')

urlpatterns = [
    
]+router.urls

