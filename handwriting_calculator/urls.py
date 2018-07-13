from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name="main_page"),
    url(r'^get_result', views.get_result, name="get_result"),
]
