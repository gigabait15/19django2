# Generated by Django 5.0.1 on 2024-02-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_students_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='email'),
        ),
    ]
