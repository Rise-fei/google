import requests
import time
import re
from collections import Counter
from lxml.html import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
proxies = {'http': 'http://lum-customer-sstrade-zone-residential-country-us:4xcrhdlj831p@zproxy.lum-superproxy.io:22225',
            'https': 'https://lum-customer-sstrade-zone-residential-country-us:4xcrhdlj831p@zproxy.lum-superproxy.io:22225'
           }
# proxies = {}


def add_data(data_results,SearchResult,word):
    for data_result in data_results:
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
                      <td><a></a></td>
                    <td><span></span></td>
                    <td><span></span></td>
                    <td><span></span></td>
                    <td><span></span></td>
                    <td><span></span></td>
                    <td><span></span></td>
                    <td><span></span></td>
                    <td><span>%s</span></td>
                    <td><button class="btn btn-default search_detail_child" type="button">详情查询</button>
                    <button class="btn btn-default delete_data_child" type="button">删除</button></td>
                 </tr>

                 '''

        lat = data_result['geometry']['location']['lat']
        lng = data_result['geometry']['location']['lng']
        name = data_result['name']
        data_html = data_html % (place_id,lat,lng,name,word)
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
            resp = requests.get(searchurl,headers=headers,proxies=proxies)
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

def getFaceAndTwit(e):
    youtube = e.xpath("//a[contains(@href,'youtube')]/@href")
    facebook = e.xpath("//a[contains(@href,'facebook')]/@href")
    twitter = e.xpath("//a[contains(@href,'twitter')]/@href")
    youtube = youtube[0] if youtube else ""
    facebook = facebook[0] if facebook else ""
    twitter = twitter[0] if twitter else ""
    count0 = 1 if youtube else 0
    count1 = 1 if facebook else 0
    count2 = 1 if twitter else 0
    return {'count':count0+count1+count2,'result':{'facebook': facebook, 'twitter': twitter,'youtube':youtube}}

# 如果有拿到联系我们的链接
def getContactWeb(u, e):
    contact1 = e.xpath("//a[contains(text(),'contact')]/@href")
    contact2 = e.xpath("//a[contains(text(),'Contact')]/@href")
    contact = contact2 + contact1
    fres = Counter(contact).keys()
    print(fres)
    if len(fres) == 0:
        return None
    else:
        u = u.split('/')[0] + '//' + [eve for eve in u.split('/')][2]
        for fr in fres:
            if fr.startswith('/'):
                if u.endswith('/'):
                    fr = u + fr[1:]
                else:
                    fr = u + fr
            return fr

def getContactUs(contactwebsite, fat):
    print('从联系我们抓取数据···')
    headers = {
        'cookie': 'Internationalization=CN|CNY; OriginCountry=CN; tid=UCNzrlOL7mPT3CBNlckDKTVpQcN1zmM8yrb8z05IMWO635u9rhtDANUUinqcZoUZTxRcr8ERmIAJ10Y4_FoLQm-YTii0MyPI-7KBUcRCXHXu0DwQs7_9ZxLt-a_9lQHCbaquQw2; id=kok3zl4qnqaa135r2cmo33cu; Experience=44_A|11_A; zip=60540; zipRemember=60540; uid=6dZ-cylI8UeG46ZkVgqOrw; CBH_CRATEUS=60dvGU2f20GQuIXr5qpzRQ; AKA_A2=A; ak_bmsc=998AC6E50D94755839F099550069462E1720F8C4C40A0000FDEE7A5EC89DF93A~plydCNfTyvdPpkjUtqIh3TpDvqRyKSI1aQjlGNAUQFTtl1mj6DJcTFB815wLlgUI+eWHk3GUdM0e/1uqkCYI1ZRpcs7KFzucO6RuNNve9S9o8NZhwUb1o6JcdakQSQH9YV1LPziYNeBnSKmnNwBdz7d0hiKyQ/wMHPB6UbQv6k8FBYsMWdmgn87HAvI+eP6KC+8xaF4XPWcyYU1TrOrAso+82aNVD8PpxNFZmckoFt5wVHIS6HpTzY839jQi0RVtRG; bm_sz=4778E4CAAB1DD8117B710B5F54DC5895~YAAQxPggF0ZeXMZwAQAAmow1EAfkBSNQDU/6qlNf8QwNKsYX0EyuiD3P4+oAJwJVdp4BaL+FZPjRVDTBGNWiP5wUtbWOpgRjOFi9PR0UlUAtkXgY2TmQZYH6ukrLJW6gIq/cD0PfbARjshT0dCMvuSaofHm1fHw0KpYI+nDOTO9vT/PP7zwvW1JJpbHS80/8WCTSA7MzH10=; optimizelyEndUserId=oeu1585114883721r0.8208182152869226; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22790da0b6-3fd0-4638-87fc-a49626673d1d%22; AMCVS_B9F81C8B5330A6F40A490D4D%40AdobeOrg=1; InternationalWelcome=1; wlcme=true; _ga=GA1.2.1037577580.1585114888; _gid=GA1.2.1407457072.1585114888; _abck=16864C232022F19D2E45962A786D0F10~0~YAAQxPggFwlfXMZwAQAAm7k1EAPIFoA1K5EpXc9izIRhkxxRrUk4yGkHSlY5S1fY9um143yytCh3AlDjArsogNeaLr2RrmZgswxReXZwNIn8oJCPXl6NGYbdtcm7854Cv64uq9Hfr334UpkMH+w7YrdTKrjwwGb3TZswrO3KV7QbQaehOrJ1qoSgnZgSj09rD1mxP/sfNQyUu7dwkVgSKH0zjbgLiw+iguuI4TaIIOpBTmatE3jisj9zx2EGS62Qah7Y1WOahmwbupPH30Bom3iTUI9Ya04lgMc5kdP/rkdaN+o17RFD2hPe53vSs9/MPHEt+sP2YzHUWxWAnveU~-1~-1~-1; basketID=227305865; basketIDRemember=227305865; hasBasket=1; s_ecid=MCMID%7C57774931402568054592901417630552029241; AMCV_B9F81C8B5330A6F40A490D4D%40AdobeOrg=-432600572%7CMCIDTS%7C18347%7CMCMID%7C57774931402568054592901417630552029241%7CMCAAMLH-1585719687%7C11%7CMCAAMB-1585719687%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1585122089s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2; BrowseViewTracking=; btpdb.kbMzxFN.dGZjLjQ4OTM1NjQ=REFZUw; D_IID=2C91E143-0507-35B7-B424-2FE71E755AC7; D_UID=2494419D-F06C-3606-AC3D-F1A03213AF80; D_ZID=16717EF8-F8AD-3D61-B141-B51DC34DFB88; D_ZUID=1955B36C-F28A-3617-977C-F7FA3968FF4A; D_HID=444BA707-4174-3C7E-B2D7-74820041F05B; D_SID=119.165.240.85:teyjbEqzEBCauZE2wRqN/DohTbALerwMHMZFwt29DFQ; _gcl_au=1.1.2076564738.1585114890; QuantumMetricUserID=4f553b5e510727227706c977e8c79e20; QuantumMetricSessionID=30423bff1ea53f9c5cfb26afd5c72ff8; cbt-consent-banner=CROSS-BORDER%20Consent%20Banner; _hjid=6cdc3d5c-4850-4ed2-aa4d-e89231ad6327; __RequestVerificationToken=52q5ZZk5CbBrd2M4EFgIqwzWYboR5JtOL-HpIz8GSFN5vouUSE8v3UbHhL5gyti6GTFGKak35Kw43U-kWcPJXqGryBo1; _scid=890b5574-7eab-4f10-81c6-7662a3a3ff8d; s_pers=%20s_ev46%3D%255B%255B%2527Typed%252FBookmarked%2527%252C%25271585114889726%2527%255D%255D%7C1742881289726%3B%20gpv%3Dspill%257Cfurniture%253Aliving%2520room%2520furniture%257Csofas%2520%2526%2520loveseats%7C1585117808092%3B%20s_vs%3D1%7C1585117808108%3B%20s_nr%3D1585116008113-New%7C1616652008113%3B%20s_dl%3D1%7C1585117808116%3B; bm_sv=8DBAC03B0C1677F86F6D74A55609543D~QdU9FCQ4l0xQtkzDLFSGKQnEYWsj21lzYSp4QP4oFW4EpKOLH4RrCVknIQ0YWD7iNNdGUmvx77+SSNXjPtn3Ir4HZ+DjWOeD6bI9IdgarLELEG1h7Kb88ZTkZSANEqjlY8JU2xtZEKoySbYQPfiwl+neO6rAt45kdEnK+NuMt0E=; s_sess=%20cmgvo%3DundefinedTyped%252FBookmarkedTyped%252FBookmarkedundefined%3B%20cpcbrate%3D0%3B%20s_sq%3D%3B%20s_ppvl%3Dspill%25257Cfurniture%25253Aliving%252520room%252520furniture%25257Csofas%252520%252526%252520loveseats%252C72%252C100%252C47608%252C1300%252C875%252C1680%252C1050%252C2%252CL%3B%20s_cc%3Dtrue%3B%20s_ppv%3Dspill%25257Cfurniture%25253Aliving%252520room%252520furniture%25257Csofas%252520%252526%252520loveseats%252C100%252C100%252C47608%252C950%252C875%252C1680%252C1050%252C2%252CL%3B; RT="z=1&dm=crateandbarrel.com&si=5eb7eddb-c45f-4e82-b88f-aee7a311b056&ss=k86wgxi7&sl=3&tt=acuk&bcn=%2F%2F684fc537.akstat.io%2F&ul=1aspo"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    contactResp = requests.get(contactwebsite, headers=headers, proxies=proxies).text
    contacte = etree.HTML(contactResp)
    # fat = 1说明Facebook和Twitter信息没采集完全
    print(fat['result'].keys(), '=========================')
    noget = [i for i in ['facebook', 'twitter', 'youtube','mails'] if i not in fat['result'].keys()]
    contactFAT = getFaceAndTwit(contacte)
    contactface = contactFAT['result']['facebook']
    contacttwit = contactFAT['result']['twitter']
    contactyoutb = contactFAT['result']['youtube']
    if not fat['result']['facebook']:
        fat['result']['facebook'] = contactface
    if not fat['result']['twitter']:
        fat['result']['twitter'] = contacttwit
    if not fat['result']['youtube']:
        fat['result']['youtube'] = contactyoutb
        print(fat['result'])
    if not fat['result']['mails']:
        pam = getPaMFromHtml(contactResp)
        if pam is not None:
            if pam['mails']:
                fat['result']['mails'] = pam['mails']
    return fat

# 首先拿到公司网址的全链接，查看网址中是否有联系我们
def getWebSource(website):
    # u = 'https://www.potterybarn.com/shop/furniture/sofa-sectional-collections/'
    # 获取到的info仅用于修改

    resp = requests.get(website, headers=headers, proxies=proxies)  # 首页的响应信息
    print('网站获取成功')
    res = resp.text
    # res = resp.content.decode()
    e = etree.HTML(res)
    # 捕获是否存在facebook和twitter，如果存在，给下一步一个信号不用捕获了，任何一个不存在则去联系我们找
    # 首页捕获的ft账号信息  {'count': 2, 'result': {'facebook': ['https://www.facebook.com/JohnLewisandPartners'], 'twitter': ['https://twitter.com/JLandPartners']}}
    # 从公司官网搜索youtube、facebook、twitter等信息。
    fat = getFaceAndTwit(e)
    print('首次页面抓取结果：', fat)
    # 从公司官网搜索邮箱
    pam = getPaMFromHtml(res)
    if pam != None:
        if pam['mails']:
            fat['result']['mails'] = pam['mails']
            fat['count'] += 1
    else:
        fat['result']['mails'] = []
    print(fat)
    if fat['count'] == 4:
        fat = dict(fat)
        return fat
    else:
        # 捕获是否有联系我们的链接，返回结果是一个联系我们链接也可能没有
        contactUs = getContactWeb(website, e)
        print('联系我们的链接：', contactUs)
        if contactUs == None:
            fat = dict(fat)
            return fat
        else:
            fat['contacturl'] = contactUs
            # 存在联系我们的链接，且数据不够完全访问此链接并进行数据补充
            fat = getContactUs(contactUs, fat)
    print('fat:', type(fat), fat)
    fat = dict(fat)
    return fat


def getPaMFromHtml(resp):
    pat = re.compile('>(.*?)<')
    s = ' '.join(pat.findall(resp))

    mails = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+)', s)

    mls = Counter(mails)
    print('mailAll:', [mk for mk, mv in mls.items() if len(
        mls.items()) > 5 and mv > 2 and '.jpg' not in mk and '.io' not in mk or mv and '.jpg' not in mk and '.io' not in mk])
    mailAll = ';'.join([mk for mk, mv in mls.items() if len(
        mls.items()) > 5 and mv > 2 and '.jpg' not in mk and '.io' not in mk or mv and '.jpg' not in mk and '.io' not in mk])
    if len(mailAll) != 0:
        return  {'mails': mailAll}
    else:
        return None

# 当调用这个的时候从网站源码中获取邮箱和电话（website必须是完整链接）
def getPaM(website):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        resp = requests.get(website, headers=headers, proxies=proxies)
        # print(resp.text)
        resp = resp.content.decode(resp.encoding)
        pat = re.compile('>(.*?)<')
        s = ' '.join(pat.findall(resp))

        mails = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+)', s)

        mls = Counter(mails)
        print('mailAll:', [mk for mk, mv in mls.items() if len(
            mls.items()) > 5 and mv > 2 and '.jpg' not in mk and '.io' not in mk or mv and '.jpg' not in mk and '.io' not in mk])
        mailAll = ';'.join([mk for mk, mv in mls.items() if len(
            mls.items()) > 5 and mv > 2 and '.jpg' not in mk and '.io' not in mk or mv and '.jpg' not in mk and '.io' not in mk])
        mail = mailAll
        if len(mailAll) != 0:
            return mail
        else:
            return []
    except:
        return []


if __name__ == '__main__':
    url = 'https://belfurniture.com/'
    # ret = getWebSource(url)     #  从官网搜，没有的话找联系我们接着搜  'mails': 'customerlove@lovesac.com;corporatesales@lovesac.com;careers@lovesac.com'                【】
    # print(ret)
    # print(getPaM(url))          # 从官网搜      【】
    print(get_email(url))         # 从谷歌搜索邮箱     prospectus@canaccordgenuity.com     【】
