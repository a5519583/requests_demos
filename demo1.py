import requests


url = 'http://httpbin.org/ip'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

proxy = {
    'http': '103.242.202.178:39015'
}

response = requests.get(url, headers=headers, proxies=proxy)

print(response.text)
# print(response.url)