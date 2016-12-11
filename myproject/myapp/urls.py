from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'public/$',
        view=views.CurrentDatetime.as_view(),
        name='public',
    ),
    url(
        regex=r'private/$',
        view=views.Private.as_view(),
        name='private',
    ),
]
