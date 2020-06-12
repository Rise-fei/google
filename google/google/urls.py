"""google URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from spider import views as spider_view
from django.views import static
from django.conf import settings
urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^admin/', admin.site.urls),
    url(r'^google_map/', spider_view.google),
    url(r'^bigemap/', spider_view.bigemap),
    url(r'^login/', spider_view.login),
    url(r'^login_check/', spider_view.login_check),
    url(r'^search_word/', spider_view.search_place_text),
    url(r'^search_word2/', spider_view.search_place_text2),
    url(r'^$', spider_view.google),
]
