from django.db import models

# Create your models here.
from django.db import models


class WashRoom(models.Model):
    name = models.CharField(max_length=5)
    time = models.IntegerField()

    def __str__(self):
        return self.name

