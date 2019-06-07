from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^store$', views.view_store, name='store'),
    url(r'^android$', views.android, name='android'),
]
