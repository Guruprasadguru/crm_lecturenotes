"""crm_lecturenotes URL Configuration

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
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('signup', views.signup),
    path('', views.home, name='home'),
    path('myprofile', views.myprofile,name='myprofile'),
    path('update/<id>', views.task_update,name='update'),
    path('customer', views.Customer_list.as_view(),name='customer'),
    path('activity/<id>', views.activity,name='activity'),
    path('addcustomer', views.addcustomer,name='addcustomer'),
    path('addactivity', views.addactivity,name='addactivity'),
]
