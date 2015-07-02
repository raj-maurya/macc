from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('webhub.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^peacetrack/', include('peacetrack.urls')),
)
