# Generated by Django 3.0.3 on 2020-03-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20200305_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='quotes',
            field=models.TextField(),
        ),
    ]
