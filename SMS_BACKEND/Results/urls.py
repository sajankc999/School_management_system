from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('result',ResultView,basename='result')
