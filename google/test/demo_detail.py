import requests
import json

key = '&key=' + 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
fields = '&fields=place_id,formatted_address,name,geometry'
language = '&language=zh-CN'
name = input('请输入要搜索的地点：\n')
# 第一次发送请求搜寻地点获取 地点id，方便后续地点详情使用。
url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' \
      'input=%s&inputtype=textquery&%s%s%s' % (name,key,fields,language)
res = requests.get(url)
json_str = res.content.decode()
# print(json_str)
data = json.loads(json_str)
with open(name+'_1.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)
# 获取第一次请求对应的响应中的地点id，然后发送 地点详情 请求。

try:
    place_id = data['candidates'][0]['place_id']
    url2 = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=%s%s%s%s' % (place_id, key, language, key)
    res2 = requests.get(url2)
    json_str2 = res2.content.decode()
    data2 = json.loads(json_str2)
    with open(name + '_2.json', 'w', encoding='utf-8') as f:
        json.dump(data2, f, ensure_ascii=False, indent=4)
except:
    print('当前搜索地点关键字无具体结果！')