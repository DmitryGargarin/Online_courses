# Generated by Django 3.2.5 on 2021-07-25 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_comment_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='homework',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.homework'),
            preserve_default=False,
        ),
    ]
