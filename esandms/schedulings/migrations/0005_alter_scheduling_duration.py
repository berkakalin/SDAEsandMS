# Generated by Django 4.2.6 on 2024-03-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulings', '0004_scheduling_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='duration',
            field=models.IntegerField(editable=False),
        ),
    ]
