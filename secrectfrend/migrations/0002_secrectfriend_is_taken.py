# Generated by Django 3.2.21 on 2023-11-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secrectfrend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secrectfriend',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
