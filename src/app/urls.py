from django.conf.urls import url
from app.views import scheduler, base
from app.views import public_view, user_view

app_name = 'app'
urlpatterns = [
    url(r'^$', base.index, name='home'),
    url(r'^scheduler/run$', scheduler.update_school_data),

    # public views
    url(r'^schools/$', public_view.school_list, name='school_list'),
    url(r'^schools/(?P<school_id>\d+)/$', public_view.school_detail, name='school_detail'),
    url(r'^schools/(?P<school_id>\d+)/add_to_comparison/$', public_view.add_to_comparison, name='add_to_comparison'),
    url(r'^schools/(?P<school_id>\d+)/remove_from_comparison/$', public_view.remove_from_comparison, name='remove_from_comparison'),

    url(r'^compare_schools/$', public_view.compare_schools, name='compare_schools'),

    # user views
    url(r'^bookmarks/$', user_view.bookmark_list, name='bookmark_list'),
    url(r'^bookmarks/(?P<school_id>\d+)/bookmark/$', user_view.bookmark, name='bookmark'),
    url(r'^bookmarks/(?P<school_id>\d+)/unbookmark/$', user_view.unbookmark, name='unbookmark'),
]
