from django.db import models

CATEGORIES = (
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)
# Create your models here.
class Quotes(models.Model):
    quotes = models.TextField(max_length=50)
    category = models.CharField(max_length=3, choices=CATEGORIES, default='LAB')

    def __str__(self):
        return self.quotes

