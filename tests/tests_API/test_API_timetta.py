import names
import pytest
import json

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
DEPARTMENT_ID = [
    '0a805716-a965-45df-912a-db8a296e5293',
    '1cfca443-cda2-4763-bd5f-a72ad3e1411b',
    '1f5a8d44-6500-45f0-92ef-464d1480eb99'
]


@pytest.mark.xfail
@pytest.mark.parametrize('department_id', DEPARTMENT_ID)
def test_Post_CreateUser(timetta_api, get_headers, department_id):
    """
    In test we testing request Create User (in server we can't create new user)
    """
    path = '/Users'
    headers = get_headers
    user_name = names.get_full_name()
    user_email = f'{user_name}@test.mail.chu'
    data = {'name': user_name,
            'email': user_email,
            'departmentId': department_id}
    json_data = json.dumps(data)
    response = timetta_api.post(path=path, headers=headers, data=json_data)
    assert response.status_code == 201
    assert response.json().get('name') == user_name
    assert response.json().get('email') == user_email
    assert response.json().get('departmentId') == department_id


@pytest.mark.parametrize('user_id', USER_ID)
def test_Get_Users(timetta_api, get_headers, user_id):
    """
    In test we testing request Get Users
    """
    path = f'/Users({user_id})'
    headers = get_headers
    response = timetta_api.get(path=path, headers=headers)
    assert response.status_code == 200
    assert response.json().get('id') == user_id


def test_Get_ProjectBillingTypes(timetta_api, get_headers):
    """
    In test we testing request Get ProjectBillingTypes
    """
    path = '/ProjectBillingTypes'
    headers = get_headers
    response = timetta_api.get(path=path, headers=headers)
    assert response.status_code == 200
    assert len(response.json().get('value')) == 3


@pytest.mark.parametrize('billing_type_id, user_id', [
    (BILLING_TYPE_ID[0], USER_ID[0]),
    (BILLING_TYPE_ID[1], USER_ID[1]),
    (BILLING_TYPE_ID[2], USER_ID[2]),
])
def test_Post_CreateProjects(timetta_api, get_headers, val_collector, billing_type_id, user_id):
    """
    In test we testing request Post CreateProject
    """
    path = '/Projects'
    headers = get_headers
    project_name = names.get_first_name(gender='female')
    data = {
        "name": f"{project_name}",
        "billingTypeId": f"{billing_type_id}",
        "managerId": f"{user_id}"
    }
    data_json = json.dumps(data)
    response = timetta_api.post(path=path, headers=headers, data=data_json)
    val_collector.add_collector(response.json().get("id"))
    assert response.status_code == 201
    assert response.json().get('billingTypeId') == billing_type_id
    assert response.json().get('managerId') == user_id
    assert response.json().get('name') == project_name


@pytest.mark.parametrize('project_id, user_id, organization_id', [
    (PROJECT_ID[0], USER_ID[0], ORGANIZATION_ID[0]),
    (PROJECT_ID[1], USER_ID[1], ORGANIZATION_ID[1]),
    (PROJECT_ID[2], USER_ID[2], ORGANIZATION_ID[2])
])
def test_Path_Project(timetta_api, get_headers, project_id, user_id, organization_id):
    """
    In test we testing request Patch Project
    """
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


def test_Get_Project(timetta_api, get_headers, val_collector):
    """
    In test we check Creating Projects
    """
    headers = get_headers
    for project_id in val_collector.get_collector():
        path = f"/Projects({project_id})"
        params = {'$expand': 'manager($select=id,name)', '$select': 'id,name'}
        response = timetta_api.get(path=path, params=params, headers=headers)
        assert response.status_code == 200
        assert response.json().get("id") == project_id
