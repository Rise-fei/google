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



url = 'http://www.google.com/search?q=mail+@+baidu.com&start=0'
res = requests.get(url)
print(res,res.content.decode())
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