from django.db import models
from users.models import BaseUser


# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.user.username} {self.user.email}'
