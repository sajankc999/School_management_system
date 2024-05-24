from rest_framework.routers import SimpleRouter
from .views import *
router = SimpleRouter()
router.register('events',CalenderView,basename='calender')

urlpatterns = [
    
]+router.urls
