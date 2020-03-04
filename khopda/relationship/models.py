from django.db import models

# Create your models he

class Relationship(models.Model):
    image = models.ImageField(upload_to='image/')
    title =  models.TextField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title