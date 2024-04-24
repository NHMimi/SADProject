from django.db import models
from django.contrib.auth.models import User


class AlarmSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Alarm types
    ALARM_TYPE_CHOICES = [
        ('motion', 'Motion Detector'),
        ('door_window', 'Door/Window Sensor'),
        ('smoke', 'Smoke Detector'),
        # Add more alarm types as needed
    ]
    alarm_type = models.CharField(max_length=50, choices=ALARM_TYPE_CHOICES, default='motion')

    # Notification preferences
    NOTIFICATION_METHOD_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('push', 'Push Notification'),
    ]
    notification_method = models.CharField(max_length=10, choices=NOTIFICATION_METHOD_CHOICES, default='email')
    notification_contact = models.CharField(max_length=255, blank=True)

    # Sensitivity level
    SENSITIVITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    sensitivity = models.CharField(max_length=10, choices=SENSITIVITY_CHOICES, default='medium')

    # Duration of the alarm (in seconds)
    duration = models.IntegerField(default=30)

    # Whether the alarm is active or not
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.alarm_type} (Sensitivity: {self.sensitivity}, Active: {self.active})"