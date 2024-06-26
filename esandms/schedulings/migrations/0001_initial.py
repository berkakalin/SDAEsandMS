# Generated by Django 5.0.2 on 2024-03-09 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('exams', '0001_initial'),
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('papername', models.CharField(max_length=50)),
                ('exam_start_date', models.DateTimeField()),
                ('exam_finish_date', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
                ('examid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.exam')),
                ('hallid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halls.hall')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
