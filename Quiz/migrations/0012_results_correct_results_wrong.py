# Generated by Django 5.1.1 on 2024-09-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0011_alter_results_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='correct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results',
            name='wrong',
            field=models.IntegerField(default=0),
        ),
    ]
