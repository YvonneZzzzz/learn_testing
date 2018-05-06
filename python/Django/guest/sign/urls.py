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
# from django.contrib import admin
# from sign import views    #导入sign应用views文件
from django.conf.urls import url   #配置接口路径 P129
from sign import views_if   #配置具体接口的二级目录
from sign import views_if_sec

urlpatterns = [


    #添加接口路径"/api/" P129
    # sign system interface
    # ex: /api/add_event
    url(r'^add_event/', views_if.add_event, name='add_event'),
    # ex: /api/add_guest
    url(r'^add_guest/', views_if.add_guest, name='add_guest'),
    # ex: /api/get_event_list/
    url(r'^get_event_list/', views_if.get_event_list, name='get_event_list'),
    # ex: /api/get_guest_list
    url(r'^get_guest_list', views_if.get_guest_list, name='get_guest_list'),
    # ex: /api/user_sign/
    url(r'^user_sign', views_if.user_sign, name='user_sign'),
    # ex: /api/sec_get_event_list/  添加用户验证  P184
    url(r'^sec_get_event_list', views_if_sec.get_event_list, name='sec_get_event_list'),
    # ex: /api/sec_add_event/  添加发布会接口   P191
    url(r'^sec_add_event', views_if_sec.add_event, name='sec_add_event'),
     # ex: /api/sec_user_sign/
    url(r'^sec_user_sign', views_if_sec.user_sign, name='sec_user_sign'),




]
