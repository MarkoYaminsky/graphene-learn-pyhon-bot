# Generated by Django 4.1.7 on 2023-03-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_studenthomework_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='topic',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]