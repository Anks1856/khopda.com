# Generated by Django 3.0.3 on 2020-03-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='landing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.TextField(max_length=30)),
                ('body', models.TextField(max_length=230)),
            ],
        ),
    ]
