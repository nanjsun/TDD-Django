<<<<<<< HEAD
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'lists.views.home_page', name='home'),
     url(r'^lists/the-only-list-in-the-world/$', 'lists.views.view_list',
	     name='view_list'
	     ),

#    url(r'^admin/', include(admin.site.urls)),
)
=======
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
]

>>>>>>> chapter6
