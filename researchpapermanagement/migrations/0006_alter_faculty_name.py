# Generated by Django 4.2.3 on 2023-08-01 09:27

from django.db import migrations, models
import researchpapermanagement.models


class Migration(migrations.Migration):

    dependencies = [
        ('researchpapermanagement', '0005_alter_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=30, validators=[researchpapermanagement.models.validate_name]),
        ),
    ]
