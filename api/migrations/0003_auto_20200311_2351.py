# Generated by Django 3.0.4 on 2020-03-11 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_trialinstance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trialinstance',
            old_name='executor_uri',
            new_name='executor_url',
        ),
    ]
