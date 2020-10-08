from rest_framework import viewsets

from .models import EnviaEmail
from .serializers import EmailSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = EnviaEmail.objects.all()
    serializer_class = EmailSerializer
