# Generated by Django 2.1 on 2019-11-02 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='datetime',
        ),
    ]
