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
    def sources_figo_connect(cls, user, data):
        data.update(country_code=cls.country_code)
        return cls.get_sesssion().post(
            cls._get_url('source/connect/figo/'),
            data=json.dumps(data), params={'user': user})

    @classmethod
    def asset_container(cls, user, filter):
        params = filter
        params.update(user=user, type=5)
        return cls.get_sesssion().get(
            cls._get_url('asset-container/'),
            params=params
        )

    @classmethod
    def get_accounts(cls, user, data):
        # r = cls.sources_figo_connect(user, data)
        # if r.status_code == 200:
        return cls.asset_container(user, {})
        # return r

    @classmethod
    def select_asset(cls, user, asset_id, selected):
        url = '/asset-container/%s/?user=%s' % (asset_id, user)
        r = cls.get_sesssion().put(
            cls._get_url(url), data=json.dumps({'selected': selected}))
        return r
