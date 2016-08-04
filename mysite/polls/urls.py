from django.conf.urls import url

from .import views
urlpatterns = [
    url(regex=r'^$', views=views.index, name='index')
]