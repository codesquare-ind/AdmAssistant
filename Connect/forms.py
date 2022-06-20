from django import forms
from .models import CallbackRequest

class CallbackForm(forms.ModelForm):

    class Meta:
        model = CallbackRequest
        fields = ('name', 'phone')