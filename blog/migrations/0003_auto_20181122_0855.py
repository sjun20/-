# Generated by Django 2.1.3 on 2018-11-21 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181122_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reserve',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
