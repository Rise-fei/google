from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests
import json
import time
from django.conf import settings
# Create your views here.
def google(request):
    return render(request,'google.html')
def test(request):
    print(1)
    return render(request,'test.html')

def search_word(request):
    # 获取地图中心的经纬度坐标
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')
    word = request.POST.get('word')
    key = '&key=' + 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
    fields = '&fields=place_id,formatted_address,name,types,geometry'
    language = '&language=zh-CN'
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' \
          'input=%s&inputtype=textquery&%s%s%s' % (word, key, fields, language)
    res = requests.get(url)
    json_str = res.content.decode()
    # print(json_str)
    data = json.loads(json_str)

    if len(data['candidates']) == 0:
        print('没有搜索到具体位置')

    else:
        path = settings.BASE_DIR + '\\json_data\\search_place\\' + word + '_place.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        # 获取第一次请求对应的响应中的地点id,然后发送 地点详情 请求。

    try:
        place_id = data['candidates'][0]['place_id']
        url2 = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=%s%s%s%s' % (place_id, key, language, key)
        res2 = requests.get(url2)
        json_str2 = res2.content.decode()
        data2 = json.loads(json_str2)
        path = settings.BASE_DIR + '\json_data\\search_place_detail\\' + word + '_detail.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data2, f, ensure_ascii=False, indent=4)
        data_result = data2['result']
        data_html = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
        d_name = data_result.get('name',"")
        d_email = data_result.get('email', "")
        d_type = data_result.get('type', "")
        d_website = data_result.get('url',"")
        d_addr = data_result.get('formatted_address',"")
        d_phone = data_result.get('formatted_phone_number',"")
        d_facebook = data_result.get('facebook',"")
        d_youtube = data_result.get('youtube',"")
        d_twitter = data_result.get('twitter',"")
        d_search_word = word
        data_html = data_html % (d_name,d_website,d_email,d_type,d_addr,d_phone,d_facebook,d_youtube,d_twitter,d_search_word)

        ret = {
            'status':1,
            'place_id':place_id,
            'msg':'成功搜索到%s对应的具体位置'%word,
            'data':data2,
            'data_html':data_html,
        }
    except:
        print('当前搜索地点关键字无具体结果,即将搜索附近结果！')
        location = '&location=%s,%s' % (lat,lng)
        radius = '&radius=50000'
        query = word
        # 第一次发送请求搜寻地点获取 地点id,方便后续地点详情使用。
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' \
              'query=%s%s%s%s%s' % (query, key, language, location, radius)
        print(url)
        # https://maps.googleapis.com/maps/api/place/textsearch/json?
        # query=空气压缩机&key=AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU&language=zh-CN
        # &location=40.0509597,116.3007982&radius=50000

        # https://maps.googleapis.com/maps/api/place/textsearch/json?
        # query=空气压缩机&key=AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU&language=zh-CN
        # &location=37.09024,-95.712891&radius=50000
        res = requests.get(url)
        json_str = res.content.decode()
        # print(json_str)
        data = json.loads(json_str)
        path = settings.BASE_DIR + '\\json_data\\search_place_nearby_list\\' + query + '_near_by_list.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        if len(data['results']) == 0:
            ret = {
                'status':-1,
                'msg':'no data'
            }
        else:
            data_final_html = ""
            data_results_list = data.get('results') # 获取列表
            for data_result in data_results_list:
                data_html = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
                d_name = data_result.get('name', "")
                d_email = data_result.get('email', "")
                d_type = data_result.get('type', "")
                d_website = data_result.get('url', "")
                d_addr = data_result.get('formatted_address', "")
                d_phone = data_result.get('formatted_phone_number', "")
                d_facebook = data_result.get('facebook', "")
                d_youtube = data_result.get('youtube', "")
                d_twitter = data_result.get('twitter', "")
                d_search_word = word
                data_html = data_html % (d_name, d_website, d_email, d_type, d_addr, d_phone, d_facebook, d_youtube, d_twitter, d_search_word)
                data_final_html += data_html
            ret = {
                'status': 0,
                'place_id': None,
                'msg': '未成功搜索到%s对应的具体位置,查询到关键字附近的搜索结果' % word,
                'data': data,
                'data_final_html':data_final_html,
            }

    return JsonResponse(ret)

def search_detail(place_id,word):
    key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
    language = 'zh-CN'
    fields = 'address_component,adr_address,business_status,formatted_address,geometry,icon,name,permanently_closed,photo,place_id,plus_code,type,url,utc_offset,vicinity,' \
             'price_level,rating,review,user_ratings_total,' \
             'formatted_phone_number,international_phone_number,opening_hours,website'
    url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=%s&key=%s&language=%s&fields=%s' % (place_id, key, language, fields)
    res = requests.get(url)
    json_str = res.content.decode()
    data = json.loads(json_str)
    # print(data)
    path = settings.BASE_DIR + '\json_data\\search_place_detail\\' + word + '_detail.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    data_result = data['result']
    data_html = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
    d_name = data_result.get('name', "")
    d_email = data_result.get('email', "")
    d_type = data_result.get('type', "")
    d_website = data_result.get('website', "")
    d_addr = data_result.get('formatted_address', "")
    d_phone = data_result.get('formatted_phone_number', "")
    d_facebook = data_result.get('facebook', "")
    d_youtube = data_result.get('youtube', "")
    d_twitter = data_result.get('twitter', "")
    d_search_word = word
    data_html = data_html % (
    d_name, d_website, d_email, d_type, d_addr, d_phone, d_facebook, d_youtube, d_twitter, d_search_word)
    # print(data_html)
    ret = {
        'status': 1,
        'place_id': place_id,
        'msg': '成功搜索到%s对应的具体位置' % word,
        'data': data,
        'data_html': data_html,
    }
    return ret

def search_near_by(lat,lng,word,radius):
    # 如果第一次的text 搜索没有结果,那么执行附近搜索
    print('当前搜索地点关键字无具体结果,即将搜索附近结果！')
    location = '%s,%s' % (lat, lng)
    radius = radius
    query = word
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
    # data['test'] = [1,2,3]
    print(len(data['results']))

    if len(data['results']) == 0:
        print('nonono data')
        ret = {
            'status': -1,
            'msg': '附近搜索没有结果'
        }
    else:
        next_page_token = data.get('next_page_token')

        while next_page_token:
            time.sleep(1)
            print(len(data['results']))
            print('下一页的token：%s' % next_page_token)
            # data['test'].extend([1,2])
            print('还有数据，接着请求！')
            key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
            next_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&pagetoken=%s" % (key, next_page_token)
            next_res = requests.get(next_url)
            next_json_str = next_res.content.decode()
            next_data = json.loads(next_json_str)
            print(data)
            print(next_data)
            data['results'].extend(next_data['results'])

            next_page_token = next_data.get('next_page_token')
            print(next_page_token)
        print('*************************')

        path = settings.BASE_DIR + '\\json_data\\search_place_nearby_list\\' + query + '_near_by_list.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


        data_final_html = ""

        data_results_list = data.get('results')  # 获取列表
        for data_result in data_results_list:
            place_id = data_result.get('place_id', '')
            ret = search_detail(place_id, word)
            data_final_html += ret.get('data_html', '')



        ret = {
            'status': 0,
            'msg': '查询到%s附近的搜索结果' % word,
            'data': data,
            'data_final_html': data_final_html,
        }
    return ret

# 精准搜索
def search_place_text(request):
    # 获取地图中心的经纬度坐标
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')
    word = request.POST.get('word')
    radius = request.POST.get('radius')
    key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
    fields = 'place_id,formatted_address,name,types,geometry'
    language = 'zh-CN'
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' \
          'input=%s&inputtype=textquery&key=%s&fields=%s&language=%s' % (word, key, fields, language)
    res = requests.get(url)
    json_str = res.content.decode()
    data = json.loads(json_str)
    print(111111)
    if len(data['candidates']) == 0:
        print('没有搜索到具体位置,即将搜索附近位置')
        ret = search_near_by(lat,lng,word,radius)
    else:
        # 搜索到具体位置了。
        path = settings.BASE_DIR + '\\json_data\\search_place\\' + word + '_place.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        # 获取第一次请求对应的响应中的地点id,然后发送 地点详情 请求。
        try:
            # 获取第一次请求对应的响应中的地点id,然后发送 地点详情 请求,获取相应数据。
            place_id = data['candidates'][0]['place_id']
            ret = search_detail(place_id,word)
        except:
            ret = {}
            pass

    return JsonResponse(ret)


# 附近搜索
def search_place_text2(request):
    # 获取地图中心的经纬度坐标
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')
    word = request.POST.get('word')
    radius = request.POST.get('radius')
    ret = search_near_by(lat,lng,word,radius)
    return JsonResponse(ret)



