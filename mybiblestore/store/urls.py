from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^about$',views.about, name='about'),
	url(r'^contact$',views.contact, name='contact'),
	url(r'^store/?$',views.store, name='store'),
	url(r'^(?i)store/(?P<item_name>[^/]+)$',views.store_item, name='store_item'),
	url(r'^$',views.index, name='index'),
	]