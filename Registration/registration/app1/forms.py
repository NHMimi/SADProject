from django import forms
from .models import AlarmSetting


class AlarmSettingForm(forms.ModelForm):
    class Meta:
        model = AlarmSetting
        fields = ['alarm_type', 'notification_method', 'notification_contact',
                  'sensitivity', 'duration', 'active']
