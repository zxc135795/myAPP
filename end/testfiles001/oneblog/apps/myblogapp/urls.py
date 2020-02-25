# ProjectName:Ltestfiles001
# FileName:urls
# author:asus
# datetime:2020/2/24 12:42
# software: PyCharm


from django.conf.urls import url
from . import views

# from .feed import *
app_name = 'myblogapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^favicon.ico/$', views.favicon),
    url(r'^list/$', views.list, name='list'),
    url(r'^about/$', views.aboutme, name='about'),
    url(r'^note/$', views.note, name='note'),

    # url(r'^rss/$',ArticleFeed(), name="rss"),
    # url(r'^allblog/$', views.allblog, name='allblog'),

]
