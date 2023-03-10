# Generated by Django 4.1.7 on 2023-03-02 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('telegram_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentgroup')),
            ],
        ),
    ]
