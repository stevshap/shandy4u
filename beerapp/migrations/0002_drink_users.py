# Generated by Django 2.2.7 on 2019-12-09 15:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
