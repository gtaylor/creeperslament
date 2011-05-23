from django.conf.urls.defaults import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name="pages/index.html"),
        name='home'),
    url(r'^get_playing/',
        TemplateView.as_view(template_name="pages/get_playing.html"),
        name='pages-get_playing'),
    url(r'^payment_received/',
        TemplateView.as_view(template_name="pages/payment_received.html"),
        name='pages-payment_received'),
)
