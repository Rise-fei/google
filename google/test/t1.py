# import requests,json
#
# def search_near_by_latlng(lat, lng, word, radius):
#     location = '%s,%s' % (lat, lng)
#     radius = radius
#     query = word
#     key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
#     language = 'en'
#     # 第一次发送请求搜寻地点获取 地点id,方便后续地点详情使用。
#     url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&language=%s&keyword=%s&key=%s' \
#           % (location, radius, language, query, key)
#     res = requests.get(url)
#     print(url)
#     json_str = res.content.decode()
#     data = json.loads(json_str)
#     print(data)
#     with open('te111.json','w',encoding='utf-8') as f:
#         json.dump(data,f,ensure_ascii=False,indent=4)
#     return data
#
# def search_detail(place_id, word):
#     key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
#     language = 'en'
#     fields = 'address_component,adr_address,business_status,formatted_address,geometry,icon,name,permanently_closed,photo,place_id,plus_code,type,url,utc_offset,vicinity,' \
#              'price_level,rating,review,user_ratings_total,' \
#              'formatted_phone_number,international_phone_number,opening_hours,website'
#     url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=%s&key=%s&language=%s&fields=%s' % (
#     place_id, key, language, fields)
#     res = requests.get(url)
#     json_str = res.content.decode()
#     data = json.loads(json_str)
#     with open('tes222.json','w',encoding='utf-8') as f:
#         json.dump(data,f,ensure_ascii=False,indent=4)
#
# # res = search_near_by_latlng(40,116,'sofa',50000)
# # print(res)
# search_detail('ChIJBfX3EW2F8TURsoFsxlQNd0Y','sofa')



#
# import re,json
# reg = re.compile(u'[\u4e00-\u9fa5]')  #检查中文
# contents =  {
#             "business_status": "OPERATIONAL",
#             "geometry": {
#                 "location": {
#                     "lat": 39.86034799999999,
#                     "lng": 116.466579
#                 },
#                 "viewport": {
#                     "northeast": {
#                         "lat": 39.86180697989271,
#                         "lng": 116.4679652298928
#                     },
#                     "southwest": {
#                         "lat": 39.85910732010727,
#                         "lng": 116.4652655701073
#                     }
#                 }
#             },
#             "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/shopping-71.png",
#             "id": "6988d4900d5bb746e6fbbd5644d45116d716e7e3",
#             "name": "芝华仕",
#             "place_id": "ChIJW7_g4Ymy8TUReGTqIiLjeyc",
#             "plus_code": {
#                 "compound_code": "VF68+4J Chaoyang, Beijing, China",
#                 "global_code": "8PFRVF68+4J"
#             },
#             "rating": 0,
#             "reference": "ChIJW7_g4Ymy8TUReGTqIiLjeyc",
#             "scope": "GOOGLE",
#             "types": [
#                 "furniture_store",
#                 "home_goods_store",
#                 "point_of_interest",
#                 "store",
#                 "establishment"
#             ],
#             "user_ratings_total": 0,
#             "vicinity": "Beijing, Chaoyang, 大羊坊路居然之家4号楼4-3-017室"
#         }
# # contents =  'hello\n年后'
# # contents = 'dsfa哈sjkl'
# print(json.dumps(contents,ensure_ascii=False))
# match = reg.search(json.dumps(contents,ensure_ascii=False))
# # match = reg.search(contents)
# if match:
#   print(contents)
# else:
#   print(u'没有包含中文')

a = [{'b': 2}, {'c': 3}, 'a', {'a': 1}, {'a': 1}]
for index,data in enumerate(a):
    print(a[index])
    print(data)
    if index == 3:
        a.pop(index)
print(a)


