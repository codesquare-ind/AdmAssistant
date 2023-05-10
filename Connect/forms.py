from django.forms import ModelForm
from .models import CallbackRequest


class ContactForm(ModelForm):
    class Meta:
        model = CallbackRequest
        fields = '__all__'