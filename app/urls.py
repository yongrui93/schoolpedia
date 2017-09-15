from django.conf.urls import url, include
from app.views import base

urlpatterns = [
    url(r'^$', base.index),
]
