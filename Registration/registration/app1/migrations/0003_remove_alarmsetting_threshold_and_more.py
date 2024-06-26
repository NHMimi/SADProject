# Generated by Django 5.0.3 on 2024-04-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_alarmsetting_alarm_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarmsetting',
            name='threshold',
        ),
        migrations.AddField(
            model_name='alarmsetting',
            name='activation_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alarmsetting',
            name='deactivation_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alarmsetting',
            name='duration',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='alarmsetting',
            name='notification_contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='alarmsetting',
            name='notification_method',
            field=models.CharField(choices=[('email', 'Email'), ('sms', 'SMS'), ('push', 'Push Notification')], default='email', max_length=10),
        ),
        migrations.AddField(
            model_name='alarmsetting',
            name='sensitivity',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10),
        ),
    ]
