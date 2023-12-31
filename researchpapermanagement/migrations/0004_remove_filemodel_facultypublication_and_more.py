# Generated by Django 4.2.3 on 2023-07-31 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchpapermanagement', '0003_alter_faculty_password_alter_student_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemodel',
            name='facultyPublication',
        ),
        migrations.RemoveField(
            model_name='filemodel',
            name='studentPublication',
        ),
        migrations.AddField(
            model_name='filemodel',
            name='author',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filemodel',
            name='by',
            field=models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
