# Generated by Django 4.2.13 on 2024-05-23 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0001_initial'),
        ('Results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authUser.student'),
        ),
    ]