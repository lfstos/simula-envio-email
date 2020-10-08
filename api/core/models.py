from django.db import models

class EnviaEmail(models.Model):
    de = models.CharField(max_length=100)
    para = models.CharField(max_length=100)
    msg = models.TextField()
    anexo = models.FileField(null=True)
