"""
URL configuration for e_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from functools import partial

from django.contrib import admin
from django.urls import path
from Product import views


urlpatterns = [
    path('', views.home, name='home'),
    path('base',views.base,name='base'),
    path('signup',views.signup,name="signup"),
path('view',views.viewed,name="viewed"),
    path('badview',views.bad_view,name="bad_view"),

    path('login',views.logins,name="logins"),
path('contactus',views.contactus,name="contactus"),
    path('products/<int:pk>/',views.product_detail,name='product_detail'),
    path('products/',views.product_list),
    path('homes', views.homes,name='homes'),
    path('admin/', admin.site.urls),
]
