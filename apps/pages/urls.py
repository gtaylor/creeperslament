from django.conf.urls.defaults import *
from django.views.generic import TemplateView
import views

urlpatterns = patterns('',
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    # Sent this out in a mailing list mail, so already accumulating
    # backwards-compatibiltiy cruft!
    # TODO: Remove this after most players have signed up.
    url(r'^get_playing/',
        TemplateView.as_view(template_name="pages/registration.html"),
        name='pages-get_playing'),
    url(r'^registration/',
        TemplateView.as_view(template_name="pages/registration.html"),
        name='pages-registration'),
    url(r'^payment_received/',
        TemplateView.as_view(template_name="pages/payment_received.html"),
        name='pages-payment_received'),
    url(r'^getting_started/',
        TemplateView.as_view(template_name="pages/getting_started.html"),
        name='pages-getting_started'),
    url(r'^useful_resources/',
        TemplateView.as_view(template_name="pages/useful_resources.html"),
        name='pages-useful_resources'),
    url(r'^support/',
        TemplateView.as_view(template_name="pages/support.html"),
        name='pages-support')
)
