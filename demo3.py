import requests

url = 'https://www.baidu.com'

response = requests.get(url)
print(response.cookies.get_dict())