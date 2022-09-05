import pytest
import requests


class Token:
    def __init__(self, auth_url):
        self.auth_url = auth_url

    def get_token(self, params=None, data=None, json=None, headers=None):
        url = f'{self.auth_url}'
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path="/", params=None, headers=None, cookies=None):
        url = f"{self.base_url}{path}"
        return requests.get(url=url, params=params, headers=headers, cookies=cookies)

    def post(self, path="/", params=None, data=None, json=None, headers=None, cookies=None):
        url = f"{self.base_url}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=headers, cookies=cookies)

    def put(self, path="/", params=None, data=None, json=None, headers=None, cookies=None):
        url = f"{self.base_url}{path}"
        return requests.put(url=url, params=params, data=data, json=json, headers=headers, cookies=cookies)

    def patch(self, path="/", params=None, data=None, json=None, headers=None, cookies=None):
        url = f"{self.base_url}{path}"
        return requests.patch(url=url, params=params, data=data, json=json, headers=headers, cookies=cookies)

    def delete(self, path="/", params=None, data=None, json=None, headers=None, cookies=None):
        url = f"{self.base_url}{path}"
        return requests.delete(url=url, params=params, data=data, json=json, headers=headers, cookies=cookies)


@pytest.fixture()
def timetta_api():
    return ApiClient(base_url='https://api.timetta.com/odata')


@pytest.fixture(scope="session")
def timetta_token():
    return Token(auth_url='https://auth.timetta.com/connect/token')
