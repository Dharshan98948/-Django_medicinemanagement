# Generated by Django 2.2.28 on 2022-12-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0009_auto_20221210_1307'),
    ]

    operations = [
        migrations.DeleteModel(
            name='signup',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='expdate',
            field=models.DateField(max_length=7, null=True),
        ),
    ]
