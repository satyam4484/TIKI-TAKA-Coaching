# Generated by Django 3.2.6 on 2021-09-29 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coach', '0001_initial'),
        ('Players', '0005_auto_20210929_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerdata',
            name='CoachName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coach.coachdata'),
        ),
    ]
