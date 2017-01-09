import datetime

from django.http import HttpResponse
from django.template import loader
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

def my_custom_page_not_found_view(request):
    template = loader.get_template('myapp/404.html')
    context = {}
    return HttpResponse(template.render(context, request), status=404)

def my_custom_error_view(request):
    template = loader.get_template('myapp/500.html')
    context = {}
    return HttpResponse(template.render(context, request), status=500)
