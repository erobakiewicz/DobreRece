from django import forms

from charity.models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DonationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)
