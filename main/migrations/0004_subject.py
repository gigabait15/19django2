# Generated by Django 4.2.4 on 2024-02-09 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_students_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.students', verbose_name='студент')),
            ],
            options={
                'verbose_name': 'предмет',
                'verbose_name_plural': 'предметы',
                'ordering': ('title',),
            },
        ),
    ]
