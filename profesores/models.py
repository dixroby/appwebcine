from django.db import models
from django.contrib.auth.models import User

class Profesor(User):
    especialidad = models.CharField(max_length=200)


class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo = models.TextField()