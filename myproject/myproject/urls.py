from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout as django_logout
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^{}/'.format(settings.ADMIN_URL), admin.site.urls),

    url(r'^logout/$', django_logout,
         {'next_page': '/'},
         name='myproject_logout'),

    #url(r'login/$',
    #    RedirectView.as_view(pattern_name='openid_with_op_name', permanent=False),
    #    {'op_name': settings.OP_NAME},
    #    name='myproject_login'),

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
