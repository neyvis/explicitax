# Generated by Django 3.2.21 on 2023-11-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secrectfrend', '0010_auto_20231115_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secrectfriend',
            name='i_took',
        ),
        migrations.RemoveField(
            model_name='secrectfriend',
            name='is_taken',
        ),
    ]
