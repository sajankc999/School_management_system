# Generated by Django 4.2.13 on 2024-05-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_courses_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
