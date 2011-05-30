from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

#sitemaps = {
#    'blog': BlogSitemap,
#}

admin.autodiscover()

urlpatterns = patterns('',
    # Standard Pages
    url(r'^', include('apps.pages.urls')),
    url(r'^account/', include('apps.account.urls')),

    # Django Admin Interface
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Sitemap
    #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
    # Serve Media via Django
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^', include('mediasync.urls')),
    )

"""
Add global template tags.
"""
from django.template import add_to_builtins
add_to_builtins('mediasync.templatetags.media')
