# Generated by Django 2.2.28 on 2022-12-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0010_auto_20221213_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='User',
        ),
    ]
