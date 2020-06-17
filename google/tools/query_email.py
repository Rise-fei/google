import requests
import time
import re
from collections import Counter

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