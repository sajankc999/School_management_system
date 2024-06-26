# Generated by Django 4.2.13 on 2024-05-23 05:42

import Assignment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.batch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.mycourses')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmitAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('assignment_content', models.FileField(upload_to='assignments/', validators=[Assignment.models.validate_file_extension])),
                ('remarks', models.TextField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assignment.assignment')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_checked', models.CharField(choices=[('Not Checked', 'Not Checked'), ('Incomplete', 'Incomplete'), ('Complete', 'Complete')], default='Not Checked', max_length=55)),
                ('remarks', models.TextField()),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('submitted_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assignment.submitassignment')),
            ],
        ),
    ]
