"""courier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from courierapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('trc/',views.trackpage),
    path('is/',views.insepage),
    path('aboutus/',views.aboutpage),
    path('conus/',views.contactpage),
    path('trackdisp/',views.tdisp),
    path('owner/',views.logpage),
    path('logc/',views.logc),
    path('newship/',views.shipment),
    path('member/',views.memberpage),
    path('reg/',views.regpage),
    path('datasave/',views.member_save_View),
    path('mlogc/',views.logcheck),
    path('comp/',views.cmpsave),
    path('workfind/',views.findview),
    path('work/',views.workpage),
    path('deleteview/',views.deleteview),
    path('all/',views.dispall),
    path('out/',views.logoutview),
]
