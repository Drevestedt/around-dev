from django import forms

SERVICE_CHOICES = [
  ('consultation', 'Consultation'),
  ('fullstack', 'Fullstack Web page/app'),
  ('frontend', 'Frontend Web page/app'),
  ('backend', 'Backend project'),
  ('maintenance', 'Maintenance of Web page/app')
]

class SelectService(forms.Form):
    please_choose_one_or_more_services = forms.MultipleChoiceField(
      choices=SERVICE_CHOICES,
      widget=forms.CheckboxSelectMultiple,
      required=False
    )