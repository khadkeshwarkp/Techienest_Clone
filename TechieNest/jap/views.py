from django.shortcuts import render
from .forms import TrainingRegistrationFormForm
from .models import TrainingRegistrationForm
from django.views.generic.edit import CreateView

def register(request):
    if request.method == 'POST':
        form = TrainingRegistrationFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = TrainingRegistrationFormForm()
    return render(request, 'jap/registerform.html', {'form': form})