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
    path('httpresponse1/',views.httpresponse1,name='httpresponse1'),
    path('httpresponse2/',views.httpresponse2,name='httpresponse2'),
    path('httpresponse3/',views.httpresponse3,name='httpresponse3'),
    path('httpresponse4/',views.httpresponse4,name='httpresponse4'),
    path('httpresponse5/',views.httpresponse5,name='httpresponse5'),
    path('httpresponse6/',views.httpresponse6,name='httpresponse6'),
    path('jsonresponse1/',views.jsonresponse1,name='jsonresponse1'),
    path('jsonresponse2/',views.jsonresponse2,name='jsonresponse2'),
    path('jsonresponse3/',views.jsonresponse3,name='jsonresponse3'),
    path('jsonresponse4/',views.jsonresponse4,name='jsonresponse4'),
    path('jsonresponse5/',views.jsonresponse5,name='jsonresponse5'),
    path('jsonresponse6/',views.jsonresponse6,name='jsonresponse6'),
    path('render1/',views.render1,name='render1'),
    path('render2/',views.render2,name='render2'),
    path('redirect1/',views.redirect1,name='redirect1'),
    path('redirect2/',views.redirect2,name='redirect2'),
    path('redirect3/',views.redirect3,name='first'),
    path('redirect4/<int:x>/',views.redirect4,name='redirect4'),
    path('redirect5/<str:name>/<int:age>/<slug:add>/',views.redirect5,name='redirect5'),
    path('redirect6/',views.redirect6,name='redirect6'),
    path('redirect7/',views.redirect7,name='redirect7'),
]
