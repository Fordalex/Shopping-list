# Generated by Django 3.0.6 on 2020-06-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.CharField(default='alexford', max_length=200),
        ),
    ]
