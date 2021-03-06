# Generated by Django 3.2.5 on 2021-07-22 07:35

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='task',
        ),
        migrations.AddField(
            model_name='lecture',
            name='task',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='presentation',
            field=models.FileField(upload_to='uploads/presentations/', validators=[main_app.models.validate_file_extension]),
        ),
    ]
