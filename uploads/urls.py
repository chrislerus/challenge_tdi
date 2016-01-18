from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'upload/$', 'uploads.views.upload_file'),
    url(r'display/', 'uploads.views.display_file'),
    )