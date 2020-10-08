from rest_framework import routers
from .viewset import EmailViewSet

router = routers.DefaultRouter()
router.register('envia-email', EmailViewSet)
