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


@pytest.fixture(scope="session")
def timetta_api():
    return ApiClient(base_url='https://api.timetta.com/odata')


@pytest.fixture(scope="session")
def timetta_token():
    return Token(auth_url='https://auth.timetta.com/connect/token')


@pytest.fixture(scope="session")
def get_access_token(timetta_token):
    login = 'NesterovA@test-task.ru'
    password = 'gG9NfM'
    data = {
        'client_id': 'external',
        'scope': 'all offline_access',
        'grant_type': 'password',
        'username': login,
        'password': password
    }
    response = timetta_token.get_token(data=data)
    access_token = response.json()['access_token']
    return access_token


@pytest.fixture(scope="session")
def get_headers(get_access_token):
    headers = {
        'Authorization': f'Bearer {get_access_token}',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'User-Agent': 'PyCharm'
    }
    return headers


class Collector:
    def __init__(self, ar_list: list):
        self.ar_list = ar_list

    def add_collector(self, value):
        self.ar_list.append(value)

    def get_collector(self):
        return self.ar_list

    def clear_collector(self):
        return self.ar_list.clear()


@pytest.fixture(scope="session")
def val_collector():
    return Collector([])
