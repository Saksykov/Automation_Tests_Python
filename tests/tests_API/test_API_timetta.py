import names
import pytest
import json


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


USER_ID = [
    '08e5b5ae-e315-4a28-a661-1562dd6d7018',
    '1197448a-5c86-412e-af84-82b9130d0510',
    '14ef4f7f-05ae-4cd1-b6da-a3ad83db2c26'
]
BILLING_TYPE_ID = [
    '4d1a525f-3abc-4871-a64a-349c1dd3cabf',
    '584dddc1-94df-43b2-b3f3-372c02fcb016',
    'e87e0e6b-c034-45ac-8b74-bd0256f3f535'
]
ORGANIZATION_ID = [
    '06ed8b85-2c4e-42dd-a3c2-484d2c410323',
    '0c1f33de-827d-4a6e-9ab4-f3a9d0477243',
    '16667aa9-28a0-458a-8866-9785eda48636'
]
PROJECT_ID = [
    '001e0509-0e91-4a60-8efd-5005edbb15b4',
    '00257765-6401-4603-9a9b-6b183adfa874',
    '005bac3a-3019-445a-92ee-86eec96c6c5b'
]


@pytest.mark.parametrize('user_id', USER_ID)
def test_Get_Users(timetta_api, get_headers, user_id):
    path = f'/Users({user_id})'
    headers = get_headers
    response = timetta_api.get(path=path, headers=headers)
    assert response.status_code == 200
    assert response.json()['id'] == user_id


def test_Get_ProjectBillingTypes(timetta_api, get_headers):
    path = '/ProjectBillingTypes'
    headers = get_headers
    response = timetta_api.get(path=path, headers=headers)
    assert response.status_code == 200
    assert len(response.json()['value']) == 3


@pytest.mark.parametrize('billing_type_id, user_id', [
    ('4d1a525f-3abc-4871-a64a-349c1dd3cabf', '08e5b5ae-e315-4a28-a661-1562dd6d7018'),
    ('584dddc1-94df-43b2-b3f3-372c02fcb016', '1197448a-5c86-412e-af84-82b9130d0510')
])
def test_Post_CreateProjects(timetta_api, get_headers, billing_type_id, user_id):
    path = '/Projects'
    headers = get_headers
    project_name = names.get_full_name()
    data = {
        "name": f"{project_name}",
        "billingTypeId": f"{billing_type_id}",
        "managerId": f"{user_id}"
    }
    data_json = json.dumps(data)
    response = timetta_api.post(path=path, headers=headers, data=data_json)
    assert response.status_code == 201
    assert response.json()['billingTypeId'] == billing_type_id
    assert response.json()['managerId'] == user_id
    assert response.json()['name'] == project_name


@pytest.mark.parametrize('project_id, user_id, organization_id', [
    (PROJECT_ID[0], USER_ID[0], ORGANIZATION_ID[0]),
    (PROJECT_ID[1], USER_ID[1], ORGANIZATION_ID[1])
])
def test_Path_Project(timetta_api, get_headers, project_id, user_id, organization_id):
    path = f'/Projects({project_id})'
    headers = get_headers
    data = {
        'managerId': f'{user_id}',
        'organizationId': f'{organization_id}'
    }
    data_json = json.dumps(data)
    response = timetta_api.patch(path=path, headers=headers, data=data_json)
    assert response.status_code == 204
    assert response.text == ''
