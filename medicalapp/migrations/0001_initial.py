# Generated by Django 2.2.28 on 2022-12-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('medicine', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
            ],
        ),
    ]
