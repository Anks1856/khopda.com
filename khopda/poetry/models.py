from django.db import models


CATEGORIES = (
    ('LOV', 'Love'),
    ('MOT', 'Motivational'),
    ('ATD', 'Attitude'),
    ('LIF', 'Life'),
    ('FRD', 'Friendship'),
    ('GOD', 'Gods'),
    ('MOM', 'Mother'),
    ('NAT', 'Nature'),
)
# Create your models here.
class Poetry(models.Model):
    poetry = models.TextField(max_length=200)
    category = models.CharField(max_length=3, choices=CATEGORIES, default='LOV')

    def __str__(self):
        return self.poetry
