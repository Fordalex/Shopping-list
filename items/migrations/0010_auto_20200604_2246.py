# Generated by Django 3.0.6 on 2020-06-04 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0009_auto_20200604_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friends',
        ),
        migrations.AddField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='friend',
            name='user',
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
