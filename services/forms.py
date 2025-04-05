from django import forms

SERVICE_CHOICES = [
  (1, 'Consultation'),
  (2, 'Fullstack Web page/app'),
  (3, 'Frontend Web page/app'),
  (4, 'Backend project'),
  (5, 'Maintenance of Web page/app')
]

class SelectService(forms.Form):
    please_choose_one_or_more_services = forms.MultipleChoiceField(
      choices=SERVICE_CHOICES,
      widget=forms.CheckboxSelectMultiple,
      required=False
    )