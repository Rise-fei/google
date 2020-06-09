import requests
import json

def parse(url,file_name):
    res = requests.get(url)
    json_str = res.content.decode()
    data = json.loads(json_str)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return data


key = '&key=' + 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
fields = '&fields=place_id,formatted_address,name,geometry'
language = '&language=zh-CN'
name = input('请输入要搜索的地点：\n')
# 第一次发送请求搜寻地点获取 地点id，方便后续地点详情使用。
url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' \
      'input=%s&inputtype=textquery&%s%s%s' % (name,key,fields,language)
data = parse(url,name+'_search_place_id.json')

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
    print('当前搜索地点关键字无具体结果,即将搜索附近结果！')
    location = '&location=40.0509597,116.3007982'
    radius = '&radius=50000'
    query = name
    # 第一次发送请求搜寻地点获取 地点id，方便后续地点详情使用。
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' \
          'query=%s%s%s%s%s' % (query, key, language, location, radius)
    res = requests.get(url)
    json_str = res.content.decode()
    # print(json_str)
    data = json.loads(json_str)
    with open(query + '_place_search.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)