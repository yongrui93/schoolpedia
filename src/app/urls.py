from django.conf.urls import url
from app.views import scheduler, base

urlpatterns = [
    url(r'^$', base.index),
    url(r'^scheduler/run$', scheduler.update_school_data),
]
