# Generated by Django 3.0.4 on 2020-03-11 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrialInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('session_id', models.CharField(blank=True, max_length=128, null=True)),
                ('executor_uri', models.CharField(blank=True, max_length=128, null=True)),
                ('trial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Trial')),
            ],
        ),
    ]
