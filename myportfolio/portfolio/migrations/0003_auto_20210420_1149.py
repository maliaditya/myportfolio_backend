# Generated by Django 3.2 on 2021-04-20 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210420_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='backend_technologies',
        ),
        migrations.RemoveField(
            model_name='services',
            name='frontend_technologies',
        ),
    ]