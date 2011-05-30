from django.conf.urls.defaults import *
#from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('',
    url(r'^login/',
        login, {'template_name': "accounts/login.html"},
        name='account-login'),
    url(r'^logout/',
        logout_then_login),
)
