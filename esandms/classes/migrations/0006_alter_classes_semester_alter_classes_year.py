# Generated by Django 4.2.6 on 2024-05-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_remove_classes_slug_alter_classes_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='semester',
            field=models.CharField(choices=[('İlkbahar', 'İlkbahar'), ('Sonbahar', 'Sonbahar')], max_length=8),
        ),
        migrations.AlterField(
            model_name='classes',
            name='year',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
    ]