# Generated by Django 4.2.6 on 2024-03-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_remove_exam_login_remove_exam_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
