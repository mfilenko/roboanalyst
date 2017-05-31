import json

from django import forms
from .cc_api import CCApi


class UserForm(forms.Form):
    user = forms.CharField()

    def get_selected_assets(self):
        user = self.cleaned_data.get('user')
        r = CCApi.asset_container(user, {'selected': 'true'})
        if r.status_code == 200:
            return json.loads(r.text)
        return r.text

    def get_all_assets(self):
        user = self.cleaned_data.get('user')
        r = CCApi.asset_container(user, {})
        if r.status_code == 200:
            return json.loads(r.text)
        return r.text


class GetAccountForm(forms.Form):
    user = forms.CharField()
    bank_code = forms.IntegerField()
    credentials = forms.CharField()

    def clean_credentials(self):
        credentials = self.cleaned_data.get('credentials')
        return credentials.split(',')

    def call(self):
        user = self.cleaned_data.get('user')
        bank_code = self.cleaned_data.get('bank_code')
        credentials = self.cleaned_data.get('credentials')
        r = CCApi.get_accounts(
            user, {'credentials': credentials, 'bank_code': bank_code})
        if r.status_code == 200:
            return {
                'success': True,
                'data': json.loads(r.text)
            }
        else:
            return {
                'success': False,
                'data': r.text
            }


class SelectAccountsForm(forms.Form):
    user = forms.CharField()
    assets = forms.CharField()

    def clean_assets(self):
        assets = self.cleaned_data.get('assets', '')
        return assets.split(',')

    def call(self):
        user = self.cleaned_data.get('user')
        assets = self.cleaned_data.get('assets')
        assets_updated = 0
        for i in assets:
            asset_id, selected = i.split(':')
            print asset_id, selected
            r = CCApi.select_asset(user, asset_id, selected)
            print r.text
            if r.status_code == 200:
                assets_updated += 1
        return {'assets_updated': assets_updated}


