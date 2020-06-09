import requests
import json

key = '&key=' + 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
fields = '&fields=place_id,formatted_address,name,geometry'
language = '&language=zh-CN'
location = '&location=40.0509597,116.3007982'
radius = '&radius=50000'
query = input('请输入要搜索的地点：\n')
# 第一次发送请求搜寻地点获取 地点id，方便后续地点详情使用。
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' \
      'query=%s%s%s%s%s' % (query,key,language,location,radius)
print(url)
res = requests.get(url)
json_str = res.content.decode()
# print(json_str)
data = json.loads(json_str)
with open(query+'_near_by.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

