from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # Champs personnalisés

    # Rôle de l'utilisateur
    role = models.CharField(max_length=255)

    # Autorisations de l'utilisateur
    permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='profiles',
    )

