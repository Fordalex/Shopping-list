# Generated by Django 3.0.6 on 2020-06-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20200604_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='kitchen', max_length=200),
            preserve_default=False,
        ),
    ]
