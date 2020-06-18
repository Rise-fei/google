import requests
# username = 'ceshi'
# password = 'ceshi123456'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
#     "Host": "www.sstrade.net:8080",
# }
# url = 'http://www.sstrade.net:8080/ssapi/customerlogin/?username=%s&password=%s&product=1&version=3.2' % (
# username, password)
# print(url)
#
# username = 'ceshi'
# product = 1
# url = 'http://www.sstrade.net:8080/ssapi/query_cust_auth_num?username=%s&product=%s' % (username,product)
# res = requests.get(url,headers=headers)
# response_content = res.content.decode()
# print(response_content)
# print(res)
import json
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
lat = 116
lng = 135
radius = 50000
word = '家具'
print('当前搜索地点关键字无具体结果,即将搜索附近结果！')
location = '%s,%s' % (lat, lng)
radius = radius
query = word
key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
language = 'zh-CN'
# 第一次发送请求搜寻地点获取 地点id,方便后续地点详情使用。
# url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' \
#       'query=%s&key=%s&language=%s&location=%s&radius=%s' % (query, key, language, location, radius)

# url = 'http://www.google.com/search?q=mail+@+baidu.com&start=0'
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=35,116&radius=50000&type=restaurant&keyword=家具&key=%s' % key
res = requests.get(url,headers=headers)
# print(res,res.content.decode())
data = res.content.decode()
data = json.loads(data)
with open('tststs.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# l = [{
#                 "long_name": "Chanute",
#                 "short_name": "Chanute",
#                 "types": [
#                     "locality",
#                     "political"
#                 ]
#             },
#             {
#                 "long_name": "Tioga",
#                 "short_name": "Tioga",
#                 "types": [
#                     "administrative_area_level_3",
#                     "political"
#                 ]
#             },
#             {
#                 "long_name": "Neosho County",
#                 "short_name": "Neosho County",
#                 "types": [
#                     "administrative_area_level_2",
#                     "political"
#                 ]
#             },
#             {
#                 "long_name": "Kansas",
#                 "short_name": "KS",
#                 "types": [
#                     "administrative_area_level_1",
#                     "political"
#                 ]
#             },
#             {
#                 "long_name": "美国",
#                 "short_name": "US",
#                 "types": [
#                     "country",
#                     "political"
#                 ]
#             },
#             {
#                 "long_name": "66720",
#                 "short_name": "66720",
#                 "types": [
#                     "postal_code"
#                 ]
#             },]
#
#
# for i in l:
#     if "country" in i['types']:
#         data = i['long_name']
# print(data)