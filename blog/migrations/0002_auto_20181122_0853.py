# Generated by Django 2.1.3 on 2018-11-21 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='end',
        ),
        migrations.RemoveField(
            model_name='reserve',
            name='start',
        ),
    ]