import requests

url = 'https://mail.qq.com/'

data = {
    'email':'455932358',
    'password':'770880lmmlmm'
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

session = requests.session()

session.post(url, data=data, headers=headers)

response = session.post('https://mail.qq.com/cgi-bin/frame_html?sid=UZc59w6O_NQ9cmky&r=6dfb6408cd3d8dc2828eb84e339f6ef9')

with open('github.html', 'w', encoding='utf-8') as fg:
    fg.write(response.text)
