from django.db import models
from users.models import BaseUser


# Create your models here.

class Buyer(models.Model):
    buyer_id = models.OneToOneField(BaseUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Buyer: {self.buyer_id.username}'
