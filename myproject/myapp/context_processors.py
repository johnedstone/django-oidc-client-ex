from django.conf import settings

def external_urls(requests):
    return {
            'GIT_PROJECT_URL': settings.GIT_PROJECT_URL,
    }

# vim: ai et ts=4 sw=4 sts=4
