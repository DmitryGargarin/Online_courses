# Generated by Django 3.2.5 on 2021-07-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_homework_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.CharField(default='', max_length=100),
        ),
    ]
