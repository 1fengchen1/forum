"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin
from registers.views import register,approveemil
from comments.views import comment_create
from instationmsg.views import unreadmsg,readmsg
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/', include('article.urls')), #后面是article下面的路径
    url(r'^$', views.index),
    url(r'^registers/$', register),
    url(r'^approve/(?P<code>\w+)$', approveemil),    #激活链接
    url(r'^accounts/', include('django.contrib.auth.urls')),    #登录链接
    url(r'^comment/create/$', comment_create),  #创建评论的js处理函数
    url(r'^message/list/$', unreadmsg),         #未读信息列表
    url(r'^message/read/', readmsg),           #处理已读信息
]
