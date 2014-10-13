# coding=utf-8

from filebrowser.sites import site
from django.conf.urls import patterns, include, url
from django.contrib import admin
from professors.views import professorsView
admin.autodiscover()

urlpatterns = patterns('django.contrib.flatpages.views',
    # Корень сайта / смотрит на flatpage /index/ из админки:
    url(r'^$', 'flatpage', {'url': '/index/'}, name='index'),
    ('^pages/', include('django.contrib.flatpages.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^admin/filebrowser/', include(site.urls)),

# Свои приложения: ------------------------------------------
    # Professors ------
    url(r'^professors/', professorsView),
    # -----------------
# -----------------------------------------------------------

# Свои приложения: ------------------------------------------
    # Django Basic File Manager ------
    url(r'^files/', include('django_bfm.urls')),
#    url(r'^media', ),
    # -----------------
# -----------------------------------------------------------

)
