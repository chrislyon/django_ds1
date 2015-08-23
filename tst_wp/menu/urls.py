from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
		url('^$', 'menu.views.home', name='home'),
		url('^about/$', 'menu.views.about', name='about'),
	]

