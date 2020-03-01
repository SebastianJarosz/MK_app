from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^operations/$', views.operations, name='operations'),
	url(r'^operations/(?P<operation_id>\d+)/$', views.operation, name='operation'),
]
