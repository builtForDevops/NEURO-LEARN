# Generated by Django 2.1.7 on 2019-06-12 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20190611_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_demo',
            name='uploader',
        ),
    ]
