# Generated by Django 3.0.8 on 2020-07-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingtracker', '0002_auto_20200713_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='time_starts',
            field=models.DateField(auto_now=True),
        ),
    ]
