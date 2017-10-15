from django.conf.urls import url
from django.contrib.auth import views as auth_views
from sso import views

app_name = 'sso'
urlpatterns = [
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'sso/login/index.html'},
        name='login'),
    url(r'^register/$',
        views.register,
        name='register'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^verify/(?P<token>\w+)/$',
        views.verify,
        name='verify'),
]
