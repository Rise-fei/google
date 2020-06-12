import requests
username = 'ceshi'
password = 'ceshi123456'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "Host": "www.sstrade.net:8080",
}
url = 'http://www.sstrade.net:8080/ssapi/customerlogin/?username=%s&password=%s&product=1&version=3.2' % (
username, password)
print(url)
res = requests.get(url,headers=headers)
response_content = res.content.decode()
print(response_content)
print(res)