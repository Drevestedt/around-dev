from django import forms
from .models import Service

class SelectService(forms.Form):
  please_choose_one_or_more_services = forms.ModelMultipleChoiceField(
    queryset=Service.objects.none(), # This will be set in __init__ function below
    widget=forms.CheckboxSelectMultiple,
    required=False,
  )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['please_choose_one_or_more_services'].queryset = Service.objects.all()
    self.fields['please_choose_one_or_more_services'].label_from_instance = lambda obj: f"{obj.name} - ${obj.price:.2f}/h"