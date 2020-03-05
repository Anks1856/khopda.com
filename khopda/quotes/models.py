from django.db import models

CATEGORIES = (
    ('LOV', 'Love'),
    ('MOT', 'Motivational'),
    ('ATD', 'Attitude'),
    ('LIF', 'Life'),
    ('FRD', 'Friendship'),
    ('GOD', 'Gods'),
)
# Create your models here.
class Quotes(models.Model):
    quotes = models.TextField()
    category = models.CharField(max_length=3, choices=CATEGORIES, default='LOV')

    def __str__(self):
        return self.quotes

