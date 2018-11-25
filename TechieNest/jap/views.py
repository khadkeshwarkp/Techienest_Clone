from django.shortcuts import render
from .forms import TrainingRegistrationFormForm
from .models import TrainingRegistrationForm
from django.views.generic.edit import CreateView

class RegisterFormView(CreateView):
    form_class = TrainingRegistrationFormForm
    model = TrainingRegistrationForm
    template_name = '/.html'

    def post(self, request, *args, **kwargs):
    	self.object = None
    	form_class = self.get_form_class()
    	form = self.get_form(form_class)
    	form.instance.user = request.user
    	if form.is_valid():
    		return self.form_valid(form)
    	else:
    		return self.form_invalid(form)