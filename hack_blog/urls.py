"""hack_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from django.contrib.staticfiles import views as static_views
import settings.base
from django.views.static import serve
from threads import views as forum_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogposts/$', views.post_list, name="blogview"),
    url(r'^$', views.post_list, name="index"),
    url(r'^post/new$', views.new_post, name="new_post"),
    url(r'^blog/(?P<id>\d+)/$', views.post_details, name="blogdetails"),
    url(r'^static/(?P<path>.*)$', static_views.serve),
    url(r'', include('accounts.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.base.MEDIA_ROOT}),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name="edit"),
    url(r'^popular/$', views.post_list_by_views, name="popular"),
    url(r'^api/', include('api.urls')),
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
]
