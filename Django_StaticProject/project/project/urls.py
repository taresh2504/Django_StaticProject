"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('landing/account/',views.account,name='account'),
    path('landing/search/',views.search,name='search'),
    # path('landing/bag/',views.bag,name='bag'),
    path('landing/cartpay/',views.cartpay,name='cartpay'),
    path('shopbycategory',views.shopbycategory,name='shopbycategory'),
    path('shopbycategory/hoodies/',views.hoodies,name='hoodies'),
    path('shopbycategory/hoodiesbox/',views.hoodiesbox,name='hoodiesbox'),
    path('shopbycategory/jackets/',views.jackets,name='jackets'),
    path('shopbycategory/joggers/',views.joggers,name='joggers'),
    path('shopbycategory/tshirt/',views.tshirt,name='tshirt'),
    path('shopbycategory/clear/',views.clear,name='clear'),
    path('policy/',views.policy,name='policy'),
    path('fitguide/',views.fitguide,name='fitguide'),
    path('otc/',views.otc,name='otc'),
]
