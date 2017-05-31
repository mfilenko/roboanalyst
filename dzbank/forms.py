from django import forms


class GetAccountForm(forms.Form):
    user = forms.CharField()
    credentials = forms.CharField()
