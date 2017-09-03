from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings

from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("users.urls")),
] 
