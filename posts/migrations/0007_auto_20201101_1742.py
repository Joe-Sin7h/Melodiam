# Generated by Django 3.0.7 on 2020-11-01 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_like_likenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='genre',
        ),
    ]
