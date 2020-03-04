# Generated by Django 3.0.3 on 2020-03-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='category',
            field=models.CharField(choices=[('LAB', 'labor'), ('CAR', 'cars'), ('TRU', 'trucks'), ('WRI', 'writing')], default='LAB', max_length=3),
        ),
    ]
