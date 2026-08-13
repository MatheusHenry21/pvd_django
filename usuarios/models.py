from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField(
        max_length=11,
        unique=True
        )
    telefone = models.CharField(
        max_length=11,
        blank=True,
        unique=True
        )
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()