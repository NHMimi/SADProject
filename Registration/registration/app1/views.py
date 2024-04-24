from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AlarmSetting
from .forms import AlarmSettingForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


def alarm_settings(request):
    settings = AlarmSetting.objects.filter(user=request.user)

    # Handle form submission
    if request.method == 'POST':
        form = AlarmSettingForm(request.POST)
        if form.is_valid():
            # Save the form
            alarm_setting = form.save(commit=False)
            alarm_setting.user = request.user  # Assign the user to the alarm setting
            alarm_setting.save()
            return redirect('alarm_settings')
    else:
        form = AlarmSettingForm()

    # Render the alarm settings page
    return render(request, 'alarm_settings.html', {'settings': settings, 'form': form})
