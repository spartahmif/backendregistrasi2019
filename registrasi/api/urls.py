from django.conf.urls import url
from django.urls import path

from api.views import StudentCreateView, StudentDetailView

urlpatterns = [
    url(r'^students/$', StudentCreateView.as_view(), name='students'),
    url(r'^students/(?P<id>[0-9]+)$', StudentDetailView.as_view(), name='detail'),
]