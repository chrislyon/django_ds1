from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'dj_doctest.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^data/$', 'ds.views.data', name='data'),
	url(r'^$', 'ds.views.home', name='home'),
)

