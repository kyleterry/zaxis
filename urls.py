from django.conf.urls.defaults import include
from django.contrib import admin
import dselector

admin.autodiscover()

parser = dselector.Parser()
url = parser.url

urlpatterns = parser.patterns('',
    # Examples:
    # url(r'^$', 'zaxis.views.home', name='home'),
    # url(r'^zaxis/', include('zaxis.foo.urls')),

    url(r'!', include('zaxis.books.urls')),
    url(r'admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
