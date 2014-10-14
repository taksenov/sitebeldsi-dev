# coding=utf-8
from afisha.views import afishaView
from arhiv.views import arhivView
from docs.views import docsView

from filebrowser.sites import site
from django.conf.urls import patterns, include, url
from django.contrib import admin
from info.views import infoView
from news.views import newsView
from professors.views import professorsView

from django.conf import settings
from django.conf.urls.static import static

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
    # docs ------------
    url(r'^docs/', docsView),
    # -----------------
    # info ------------
    url(r'^info/', infoView),
    # -----------------
    # news ------------
    url(r'^news/', newsView),
    # -----------------
    # afisha ----------
    url(r'^afisha/', afishaView),
    # -----------------
    # arhiv -----------
    url(r'^arhiv/', arhivView),
    # -----------------
# -----------------------------------------------------------

# Свои приложения: ------------------------------------------
    # Django Basic File Manager ------
#    url(r'^files/', include('django_bfm.urls')),
#    url(r'^media', ),
    # -----------------
# -----------------------------------------------------------

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
