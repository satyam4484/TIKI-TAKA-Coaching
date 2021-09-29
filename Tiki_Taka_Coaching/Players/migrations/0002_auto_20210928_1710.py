# Generated by Django 3.2.6 on 2021-09-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_coach',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_parent',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.AddField(
            model_name='user',
            name='UserType',
            field=models.IntegerField(default=1),
        ),
    ]
