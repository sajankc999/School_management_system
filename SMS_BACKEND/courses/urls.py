from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('course',CoursesView,basename='course')
router.register('mycourse',MycouserView,basename='mycourse')

urlpatterns = [
    
]+router.urls
