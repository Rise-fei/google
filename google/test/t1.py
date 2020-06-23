import requests,re
from collections import Counter

def getPaM(website):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        resp = requests.get(website, headers=headers,)
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




website = 'https://www.google.com/search?q=artofmanliness.com&start=20'
# mail = getPaM(website)
res = requests.get(website)
with open('res.text','w',encoding='utf-8')as f:
    f.write(res.text)
rule = re.compile('([a-zA-Z1-9_-]+@\w+\.\w{3,6})')
result = rule.findall(res.text)
print(result)
# print(mail)