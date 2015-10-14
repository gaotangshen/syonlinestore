from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url('^register/$', views.register, name="register"),
    # url('^register/success/$', views.register_success, name="register_success"),
	url('^login/$', views.login, name='login'),
	url('^$', views.home, name='home'),
	url('^password_reset/$', views.password_reset,  name='password_reset'),
] 