
from django.conf.urls import url

from post import views
from post.views import *

app_name="post"

urlpatterns = [

    url(r'^$', views.post_list, name='index'),
    # Example: /post/ (same as /)
    url(r'^my_post/$',
        views.my_post_list, name="my_post",
    ),
    url (r'^search/$', SearchFormView.as_view(), name='search'),
    url(r'^accounts/(?P<user_pk>\d+)/$', views.user_detail, name='user_detail'),
    # Example: /add/
    url(r'^add/$',
        PostCreateView.as_view(), name="add",
    ),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        PostUpdateView.as_view(), name="update",),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        PostDeleteView.as_view(), name="delete",
    ),
    url(r'^(?P<post_pk>\d+)/comment/create/$', views.comment_create, name='comment_create'),
    url(r'^my_post/(?P<post_pk>\d+)/comment/create/$', views.my_comment_create, name='my_comment_create'),
]
