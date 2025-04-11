from django import forms
from .models import Service

class SelectService(forms.Form):
  please_choose_one_or_more_services = forms.ModelMultipleChoiceField(
    queryset=Service.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=False
  )