# Generated by Django 4.2.6 on 2024-05-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_alter_classes_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='slug',
        ),
        migrations.AlterField(
            model_name='classes',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classes',
            name='year',
            field=models.IntegerField(),
        ),
    ]
