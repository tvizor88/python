import requests
import json

login_url = 'https://iot.chisw.us/auth/login'
login_data = {
    'username': 'gorshkov.sash.chi@gmail.com',
    'password': 'Aa5235524!'
}
response = requests.post(login_url, data=login_data)
if response.ok:
    print('success login!', response.text)
    response_text = response.text
    response_data = json.loads(response_text)
    access_token = response_data['access_token']
    print(response.status_code)
    print(access_token)

else:
    print('error login:', response.text)
