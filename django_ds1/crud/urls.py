"""django_ds1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url('^$', 'crud.views.crud_list', name='crud_list'),
	url('^create/$', 'crud.views.crud_create', name='crud_create' ),
	url('^update/(?P<pk>\d+)$', 'crud.views.crud_update', name='crud_update' ),
	url('^del/(?P<pk>\d+)$', 'crud.views.crud_delete', name='crud_delete' ),
]
