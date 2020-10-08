from rest_framework import serializers

from .models import EnviaEmail

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnviaEmail
        fields = ('id','de', 'para', 'msg', 'anexo')


