from django import forms
from .models import TrainingRegistrationForm

class TrainingRegistrationFormForm(forms.ModelForm):
    class Meta:
        model = TrainingRegistrationForm
        fields = ('name', 'email', 'contact_no', 'hometown', 'state', 'college', 'branch', 'current_semester', 'registration_for', 'previous_exp', 'how_did_you_know', 'techienest_contactperson')