# Generated by Django 5.0.1 on 2024-02-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='online'),
        ),
    ]