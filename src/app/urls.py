from django.conf.urls import url
from app.views import base

urlpatterns = [
    url(r'^$', base.index),
]
