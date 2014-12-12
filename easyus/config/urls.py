from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'easyus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)

admin.site.site_header = '%s Headquarters' % settings.PROJECT_NAME
admin.site.index_title = 'Base of Operations'
