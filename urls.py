from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
# url(r'^$', views.index), # This line has changed!
url(r'^$', views.index),
url(r'^checkout$', views.checkout),
url(r'^confirmation/$', views.confirmation)
]