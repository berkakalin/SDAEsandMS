# Generated by Django 4.2.6 on 2024-05-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]