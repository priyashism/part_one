from django.conf.urls import url
from one_app import views

urlpatterns = [
    url(r'^&', views.index, name='index')
]

