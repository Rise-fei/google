import requests
import time
import re
from collections import Counter
from lxml.html import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

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


def getnewmail(website):
    print(website)
    if ' ' in website:
        website = website.split(' ')[0]
        print(website)
    print('++++++++++')
    if 'www.' in website:
        newsite = website.split('www.')[1].split('/')[0]
    elif 'http' in website:
        newsite = website.split('://')[1].split('/')[0]
    else:
        newsite = website.split('/')[0]
    newsite = 'mail+@+' + newsite
    mails = googlemail(newsite)
    maildata = ';'.join(gettruest(mails))
    if len(maildata) > 5:
         return maildata
    else:
        return ''


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

def googlemail(kw):
    mailstart = 0
    while mailstart <= 20:
        time.sleep(0.2)
        searchurl = 'http://www.google.com/search?q={}&start={}'.format(kw, mailstart)
        print(searchurl)
        try:
            resp = requests.get(searchurl,headers=headers)
            print(resp)
            if '找不到和您查询' not in resp.text:  # 说明有内容
                ts = resp.text
                with open('email.html','w',encoding='utf-8') as f:
                    f.write(ts)
                rule = re.compile('([a-zA-Z1-9_-]+@\w+\.\w{3,6})')
                result = rule.findall(ts)
                mailstart += 10
                print('------------')
                print(result)
                print('------------')
                yield result
            else:
                break
        except Exception as e:
            print(e)

if __name__ == '__main__':
    url = 'https://www.leons.ca/collections/furniture-living-room-sofas&sa=U&ved=2ahUKEwjA5efcu_jlAhUDy1kKHWpkCs84ChAWMAB6BAgDEAE&usg=AOvVaw2N3Hlc3F3Cpx3Yx1HBxBbg'
    ret = getnewmail(website=url)
    print(ret)