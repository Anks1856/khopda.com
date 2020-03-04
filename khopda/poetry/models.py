from django.db import models

# Create your models here.
class Poetry(models.Model):
    poetry = models.TextField(max_length=200)

    def __str__(self):
        return self.poetry
