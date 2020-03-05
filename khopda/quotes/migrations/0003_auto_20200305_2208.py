# Generated by Django 3.0.3 on 2020-03-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quotes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='category',
            field=models.CharField(choices=[('LOV', 'Love'), ('MOT', 'Motivational'), ('ATD', 'Attitude'), ('LIF', 'Life'), ('FRD', 'Friendship'), ('GOD', 'Gods')], default='LOV', max_length=3),
        ),
    ]