"""starterupp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import urls
from django.urls import include, path
from rest_framework import routers
from starterupperupp import views
from django_otp.admin import OTPAdminSite
from rest_framework.authtoken.views import obtain_auth_token
admin.site.site_header = 'STARTER UPP'
admin.site.site_title = 'STARTER UPP'
router = routers.DefaultRouter()
router.register(r'companys', views.CompanyViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'payrates', views.PayRateViewSet)

# router.register(r'trannys', views.PieViewSet.as_view({'get': 'list'}))
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('you-would-have-never-guessed-it/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('signup/', views.signup),
    path('login/', views.login),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
]
