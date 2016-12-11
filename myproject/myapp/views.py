import datetime

from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin

class CurrentDatetime(TemplateView):
    template_name = "myapp/now.html"

    # login_url = "/accounts/login/"

    def get(self, request):
        #return self.render_to_response({})
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(CurrentDatetime, self).get_context_data(**kwargs)

        context['now'] =  datetime.datetime.now()

        return context

class Private(LoginRequiredMixin, TemplateView):
    template_name = "myapp/private.html"


    def get(self, request):
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(Private, self).get_context_data(**kwargs)

        context['now'] =  datetime.datetime.now()

        return context
