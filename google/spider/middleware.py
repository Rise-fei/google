from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import re
import requests
class LoginCheckMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print(request.session.get('is_login'))
        print(request.path_info)
        white_url = ['/login/','/login_check/','/admin/','/static/','/logout/','^$']
        for re_url in white_url:
            if re.match(re_url,request.path):
                print('路径匹配成功')
                return

        print('路径匹配不成功')
        if request.session.get('is_login'):
            session_key = request.COOKIES.get('session_key')
            if session_key:
                # 如果oa管理员通过一键下线当前客户所有终端，那么此web项目目前是不知道的，所以向主服务器发送请求查询一下
                # 但是此方法不好，该每次发送请求，都要向主服务器查询，最好改成：
                # （主服务器执行一键下线后，给当前web项目发送请求，告知当前项目哪一个客户下线了，在此web项目中加以判断）
                url = 'http://www.sstrade.net:8080/ssapi/query_is_login?session_key=%s' % session_key
                res = requests.get(url)
                if res.content.decode() == 'yes':
                    print('当前浏览器中存储的用户cookie：session_key在服务器端有对应的记录，即该用户是登录状态！')
                    return
                else:
                    print('当前浏览器中存储的用户cookie：session_key在服务器端没有对应的记录，即该用户应该下线！')
                    request.session['is_login'] = False
                    request.COOKIES['session_key'] = ""
                    return redirect('/login/')
            else:
                return redirect('/login/')

        else:
            return redirect('/login/')
