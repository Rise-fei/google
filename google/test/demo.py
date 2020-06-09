import requests
import json
key = '&key=' + 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
fields = '&fields=place_id,photos,formatted_address,name,rating,opening_hours,geometry'
language = '&language=zh-CN'
name = input()
url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%s&inputtype=textquery&%s%s%s' % (name,key,fields,language)
res = requests.get(url)
json_str = res.content.decode()
print(json_str)
data = json.loads(json_str)
with open(name+'_1.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

