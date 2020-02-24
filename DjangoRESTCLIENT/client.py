import requests

URL = "http://127.0.0.1:8000"


def get_token():
    # Authentication connection by Token
    url = f"{URL}/api/auth/"
    response = requests.post(url, data= {
        'username': 'iries', 'password':'IriesD3v3l0p3r$'
    })
    return response.json()


def get_data():
    url = f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    emp_data = response.json()
    for e in emp_data:
        print(e)

# get_data()


def create_new(count):
    url = f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    data ={
        "id": count,
        "name": f"Test{count}",
        "phone": 689672535,
        "birth": "1991-05-14",
        "employee_id": f"HQ000{count}"
    }
    response = requests.post(url, data=data, headers=header)
    print(response.text)
    print(response.status_code)

# for e in range(5, 20):
#     create_new(e)


def edit_data(employee_id):
    url = f"{URL}/api/users_list/{employee_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    data ={
        "name": f"Update Test2",
        "phone": 99999999,
        "birth": "2012-12-12",
        "employee_id": f"{employee_id}"
    }
    response = requests.put(url, data=data, headers=header)
    print(response.text)
    print(response.status_code)

# edit_data(7)


def delete_data(employee_id):
    url = f"{URL}/api/users_list/{employee_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(url, headers=header)
    print(response.status_code)


for e in range(7,17):
    delete_data(e)


