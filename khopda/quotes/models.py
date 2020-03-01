from django.db import models

# Create your models here.
class quotes(models.Model):
    quotes = models.TextField(max_length=50)