from django.db import models

# Create your models here.
class landing(models.Model):
    image = models.ImageField(upload_to="image/")
    title = models.TextField(max_length=30)
    body = models.TextField(max_length=230)