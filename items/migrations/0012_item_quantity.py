# Generated by Django 3.0.6 on 2020-06-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_auto_20200604_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]