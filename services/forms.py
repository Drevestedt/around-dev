from django import forms
from .models import Service

SERVICE_CHOICES = [
  ('consultation', 'Consultation'),
  ('fullstack', 'Fullstack Web page/app'),
  ('frontend', 'Frontend Web page/app'),
  ('backend', 'Backend project'),
  ('maintenance', 'Maintenance of Web page/app')
]

class SelectService(forms.Form):
  please_choose_one_or_more_services = forms.MultipleChoiceField(
    choices=[]
    widget=forms.CheckboxSelectMultiple,
    required=False
  )
