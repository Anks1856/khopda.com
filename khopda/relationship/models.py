from django.db import models

CATEGORIES = (
    ('LOV', 'Love'),
    ('CRS', 'Crush'),
    ('M&S', 'Mom&Son'),
    ('D&S', 'Dad&Son'),
    ('B&S', 'Brother&Sister'),
    ('BFF', 'BestFriend'),
    ('RLV', 'Relatives'),
    ('HAT', 'Hatters'),
    ('TCR', 'Teacher'),
    ('RML', 'Role Model'),
    ('SUP', 'Supporters'),
    ('COL', 'Colleague'),
)

# Create your models here

class Relationship(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.TextField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=3, choices=CATEGORIES, default='LOV')

    def __str__(self):
        return self.title

    def front(self):
        return self.body[:250]

    def contant(self):
        return self.body[250:]