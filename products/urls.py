from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),	
	url(r'^(?P<product_id>[0-9]+)/ingredients/$', views.ingredient_get, name='ingredients'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<product_id>[0-9]+)/ingredient_pick/$', views.ingredient_pick, name='ingredient_pick'),	
] 