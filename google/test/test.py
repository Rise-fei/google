import requests
import json

location = '%s,%s' % (37.96741773604804, 2554.729619189455931)
radius = 50000
query = 'sofa'
key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
language = 'zh-CN'
# 第一次发送请求搜寻地点获取 地点id,方便后续地点详情使用。
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' \
      'query=%s&key=%s&language=%s&location=%s&radius=%s' % (query, key, language, location, radius)
res = requests.get(url)
print(url)
json_str = res.content.decode()
data = json.loads(json_str)
print(data)
with open('tttttest.json','w',encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)