"""menu_exp URL Configuration

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
import restaurants.views 
import menu_exp.views
from django.contrib.auth.views import login,logout

from menu_exp.views import Index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^menu/(\d{1,5})/$',restaurants.views.menu),
    url(r'^meta/$',restaurants.views.meta),
    url(r'^welcome/$',menu_exp.views.welcome),
    url(r'^restaurants_list/$',restaurants.views.list_restaurants),
    url(r'^comment/(\d{1,5})/$',restaurants.views.comment),
    #url(r'^set_c/$',restaurants.views.set_c),
    #url(r'^get_c/$',restaurants.views.get_c),
    #url(r'^session/$',restaurants.views.use_session),
    #url(r'^t_session/$',restaurants.views.test_session),
    url(r'^accounts/login/$',login),
 #   url(r'^index/$',menu_exp.views.index),
    url(r'^index/$',Index.as_view()) ,
    url(r'register/$',menu_exp.views.register),
    url(r'^accounts/logout/$',logout)

]
