import requests,json,re
from lxml.html import etree
from collections import Counter


def getPaMFromHtml(resp):
    pat = re.compile('>(.*?)<')
    s = ' '.join(pat.findall(resp))
    print('*******************')
    print(s)
    print('*******************')
    mails = re.findall(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', s)
    print(mails)
    print(mails)
    print(mails)
    mls = Counter(mails)
    print('mailAll:', [mk for mk, mv in mls.items() if len(
        mls.items()) > 5 and mv > 2 and '.jpg' not in mk and '.io' not in mk or mv and '.jpg' not in mk and '.io' not in mk])
    mailAll = ';'.join([mk for mk, mv in mls.items() if len(
        mls.items()) > 5 and mv > 2 and '.jpg' not in mk and '.io' not in mk or mv and '.jpg' not in mk and '.io' not in mk])
    if len(mailAll) != 0:
        return  {'mails': mailAll}
    else:
        return None


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    website = 'http://smartledsupply.com/contact/'
    resp = requests.get(website, headers=headers, proxies={})  # 首页的响应信息
    print('网站获取成功')
    with open('tt.html','wb',) as f:
        f.write(resp.content)
    e = etree.HTML(resp.text)
    contact1 = e.xpath("//a[contains(text(),'contact')]/@href")
    contact2 = e.xpath("//a[contains(text(),'Contact')]/@href")
    contact3 = e.xpath("//a[contains(@href,'contact')]/@href")
    contact4 = e.xpath("//a[contains(@href,'Contact')]/@href")
    print(contact1,contact2,contact3,contact4)
    # ret2 = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+)',resp.text)
    # print(ret2)
    # ret = re.findall(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', )
    # print(ret)
    # res = resp.text
    # ret = getPaMFromHtml(res)
    # print(ret)
    # a = 'hello world hello@163.com python@456.com'
    # s = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+)',a)
    # print(s)