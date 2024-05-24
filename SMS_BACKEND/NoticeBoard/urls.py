from .views import *
from rest_framework.routers import SimpleRouter

router= SimpleRouter()
router.register('notice',NoticeBoardView,basename='notice')

urlpatterns = [
    
]+router.urls

