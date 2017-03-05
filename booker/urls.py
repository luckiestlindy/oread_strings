from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ensembles/$', views.ensembles, name='ensembles'),
    url(r'^musicians/$', views.musicians, name='musicians'),
    url(r'^listen/$', views.listen, name='listen'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^bookings/$', views.bookings, name='bookings'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    
    url(r'^selections/(?P<pk>\d+)/$', views.selectionlist_detail, name='selectionlist_detail'),
    url(r'^selections/(?P<pk>\d+)/form/$', views.selectionlist_form, name='selectionlist_form'),
    
    url(r'^send_selections/(?P<pk>\d+)/$', views.send_selections, name='send_selections'), 

    url(r'^contract/(?P<pk>\d+)/$', views.contract, name='contract'),
    url(r'^notify_players/(?P<pk>\d+)/$', views.notify_players, name='notify_players'),
    url(r'^contract/pdf/(?P<pk>\d+)/$', views.contract_pdf, name='contract_pdf'),
    url(r'^contract/link/(?P<pk>\d+)/$', views.contract_link, name='contract_link'),
    url(r'^musician/(?P<pk>\d+)/$', views.musician_detail, name='musician_detail'),
#    url(r'^drip/(?P<pk>\d+)/$', views.drip, name='drip'),
#    url(r'^email_one$', views.email_one, name='email_one'),
]
