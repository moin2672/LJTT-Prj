# Generated by Django 4.1 on 2022-08-07 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ljttcards', '0002_alter_ljttcard_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ljttcard',
            name='likes',
            field=models.ManyToManyField(related_name='ljtt_cards', to=settings.AUTH_USER_MODEL),
        ),
    ]
