# Generated by Django 3.0.4 on 2020-03-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alertas', '0002_auto_20200322_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggression',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='aggression',
            name='time',
            field=models.DateTimeField(verbose_name='date occurred'),
        ),
    ]
