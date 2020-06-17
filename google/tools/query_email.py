import requests
import time
import re
from collections import Counter


def add_data(data,SearchResult,word):
    for data_result in data['results']:
        place_id = data_result['place_id']
        type_str = ""
        for s in data_result['types']:
            type_str += s + ','

        data_html = '''
                 <tr id='%s'>
                     <td>
                          <input class='data_td' type='checkbox'>
                     </td>
                     <td><a lat='%s' lng='%s' class='search_result_name'>%s</a></td>
                     <td><p></p></td>
                     <td><p></p></td>
                     <td><p></p></td>
                     <td><p></p></td>
                     <td><p></p></td>
                     <td><p></p></td>
                     <td><p></p></td>
                     <td><p></p></td>
                     <td><p></p></td>
                 </tr>

                 '''

        lat = data_result['geometry']['location']['lat']
        lng = data_result['geometry']['location']['lng']
        name = data_result['name']
        data_html = data_html % (place_id,lat,lng,name)
        try:
            if not SearchResult.objects.filter(place_id=place_id):
                SearchResult.objects.create(name=name, type=type_str, search_word=word, place_id=place_id,
                                                      td_html=data_html)
            else:
                print('数据库中已经存在该数据，无需再次添加！！！')
        except Exception as e:
            print(e)

def googlemail(kw):
    mailstart = 0
    while mailstart <= 20:
        time.sleep(0.2)
        searchurl = 'http://www.google.com/search?q={}&start={}'.format(kw, mailstart)
        print(searchurl)
        try:
            resp = requests.get(searchurl)
            print(resp)
            if '找不到和您查询' not in resp.text:  # 说明有内容
                ts = resp.text
                rule = re.compile('([a-zA-Z1-9_-]+@\w+\.\w{3,6})')
                result = rule.findall(ts)
                mailstart += 10
                yield result
            else:
                break
        except Exception as e:
            print(e)

def gettruest(mails):
    res = [i for item in mails for i in item]
    print(res)
    mdic = Counter(res)
    print(mdic)
    final = sorted(mdic.items(), key=lambda d: d[1], reverse=True)
    print(len(final))
    print(final)
    if 0 <= len(final) < 3:
        for i in range(len(final)):
            yield final[i][0]
    else:
        for i in range(3):
            yield final[i][0]

def get_email(website):
    website = website
    if 'www.' in website:
        newsite = website.split('www.')[1].split('/')[0]
    elif 'http' in website:
        newsite = website.split('://')[1].split('/')[0]
    else:
        newsite = website.split('/')[0]
    newsite = 'mail+@+' + newsite
    print('*************')
    print(newsite)
    print('*************')

    mails = googlemail(newsite)
    print(mails)
    maildata = ';'.join(gettruest(mails))
    if len(maildata) > 5:
        print(maildata)
        return maildata
    else:
        return ""