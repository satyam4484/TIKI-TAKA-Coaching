# Generated by Django 3.2.6 on 2021-09-29 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0003_parentdata_playerdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserType',
            field=models.CharField(max_length=50),
        ),
    ]
