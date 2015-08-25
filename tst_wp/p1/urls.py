from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
		url('^$', 'p1.views.home', name='home'),
		url('^about/$', 'p1.views.about', name='about'),
		url('^f1/$', 'p1.views.f1', name='f1'),
		url('^t1/$', 'p1.views.t1', name='t1'),
	]

