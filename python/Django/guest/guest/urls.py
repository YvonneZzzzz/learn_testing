"""guest URL Configuration
# Django项目的URL声明

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

# from django.conf.urls import url
from django.contrib import admin
from sign import views    #导入sign应用views文件
# from django.conf.urls import url, include   #配置接口路径 P129
from django.conf.urls import url, include
# from sign import views_if   #配置具体接口的二级目录

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),  # 127.0.0.1：8000进去是index
    url(r'^index/$', views.index),  #添加index/路径配置
    url(r'^login_action/$', views.login_action),  #添加login_action/路径配置
    url(r'^event_manage/$', views.event_manage),  #添加event_manage/路径配置
    url(r'^accounts/login/$', views.event_manage),  #添加event_manage/路径配置
    url(r'^search_name/$',views.search_name),
    url(r'^guest_manage/$',views.guest_manage),
    url(r'^search_phone/$',views.search_phone),
    url(r'^sign_index/(?P<eid>[0-9]+)/$',views.sign_index),     #(?P<eid>[0-9]+) 匹配发布会ID，且必须为数字
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),
    url(r'^logout/$',views.logout),

    url(r'^api/', include('sign.urls', namespace="sign")),  #添加接口路径"/api/" P129

    # 添加到 guest/sign/urls.py 下
    # # sign system interface
    # # ex: /api/add_event
    # url(r'^add_event/', views_if.add_event, name='add_event'),
    # # ex: /api/add_guest
    # url(r'^add_guest/', views_if.add_guest, name='add_guest'),
    # # ex: /api/get_event_list/
    # url(r'^get_event_list/', views_if.get_event_list, name='get_event_list'),
    # # ex: /api/get_guest_list
    # url(r'^get_guest_event', views_if.get_guest_list, name='get_guest_list'),
    # # ex: /api/user_sign/
    # url(r'^user_sign', views_if.user_sign, name='user_sign'),
    
 



]
