from django.db import models

# Create your models here.
class Town(models.Model):
    town = models.CharField(max_length=30)

    def __str__(self):
        return self.town