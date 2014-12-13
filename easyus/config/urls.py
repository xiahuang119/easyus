from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)

admin.site.site_header = '%s Headquarters' % settings.PROJECT_NAME
admin.site.index_title = 'Base of Operations'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
