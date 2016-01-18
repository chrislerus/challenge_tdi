from django.conf.urls import include, url
import uploads.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'tdi_challenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(uploads.urls)),

    ]
