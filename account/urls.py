from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^register/$', views.register, name="register"),
    # url('^register/success/$', views.register_success, name="register_success"),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),	
	url(r'^password_reset/$', views.password_reset,  name='password_reset'),
] 