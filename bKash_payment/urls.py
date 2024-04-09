from rest_framework.urlpatterns import format_suffix_patterns

__author__ = 'milu'
from django.urls import path
from django.contrib.auth.decorators import login_required_custom as auth
from django.urls import include

from views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url (
           regex = '^$',
           view =  auth(home),
           name = 'bKash-home'
    ),
)

urlpatterns = format_suffix_patterns(urlpatterns)