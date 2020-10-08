from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .core.viewset import EmailViewSet
from .core.router import router

# router = routers.DefaultRouter()
# router.register('envia-email', EmailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),

]
