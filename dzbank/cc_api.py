import json
import requests


class CCApi(object):
    country_code = 'DE'
    base_url = 'https://dev-connect.core.fincite.net/api/v1/'

    @classmethod
    def get_sesssion(cls):
        if not hasattr(cls, '_session'):
            cls._session = requests.session()
            cls._session.headers.update({
                'Authorization': (
                    'Bearer 6a9828df8a8bee8cf2f2a4e85b09ba82c37e01a1'),
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            })
        return cls._session

    @classmethod
    def _get_url(cls, path):
        return cls.base_url + path

    @classmethod
    def get_accounts(cls, user, data):
        return cls.get_sesssion().post(
            'source/connect/figo/',
            data=json.dumps(data), params={'user': user})

    # GET /api/v1/source/connect/figo/supported_banks/
