# Generated by Django 3.1 on 2021-07-06 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0003_auto_20210628_0600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptom',
            name='desease_name',
        ),
    ]
