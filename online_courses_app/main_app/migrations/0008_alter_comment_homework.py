# Generated by Django 3.2.5 on 2021-07-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_comment_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='homework',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.homework'),
        ),
    ]