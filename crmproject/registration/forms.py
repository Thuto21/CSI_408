from django import forms

from registration.models import Staff


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staffid', 'name', 'phone', 'email', 'password']
