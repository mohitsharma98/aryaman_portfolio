# Generated by Django 2.1 on 2019-11-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_image', models.FileField(upload_to='')),
                ('twitterlink', models.TextField()),
                ('facebooklink', models.TextField()),
                ('instagramlink', models.TextField()),
                ('model_image', models.FileField(upload_to='')),
                ('aboutme', models.TextField(max_length=300)),
            ],
        ),
    ]
