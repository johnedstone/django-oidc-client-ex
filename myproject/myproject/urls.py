from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout as django_logout
from django.http import HttpResponse
from django.views.generic.base import RedirectView

handler404 = 'myapp.views.my_custom_page_not_found_view'
handler500 = 'myapp.views.my_custom_error_view'

urlpatterns = [
    url(r'^{}/'.format(settings.ADMIN_URL), admin.site.urls),
    url(r'^health$', lambda request:HttpResponse(status=200)),

    url(r'^logout/$', django_logout,
         {'next_page': '/'},
         name='myproject_logout'),

    url(r'openid/', include('djangooidc.urls')),

    url(r'^myapp/', include('myapp.urls', namespace='myapp')),

    url(r'^$',
        RedirectView.as_view(pattern_name='myapp:public', permanent=False),
       name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

# vim: ai et ts=4 sw=4 sts=4
