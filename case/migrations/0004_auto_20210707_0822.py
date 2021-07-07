# Generated by Django 3.1 on 2021-07-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0004_remove_symptom_desease_name'),
        ('case', '0003_auto_20210706_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='symptom_name',
            field=models.ManyToManyField(to='symptoms.Symptom'),
        ),
        migrations.DeleteModel(
            name='CaseSymptoms',
        ),
    ]
