from django.conf.urls import url, include
from django.urls import path

from api.views import StudentCreateView, StudentDetailView

urlpatterns = [
    url(r'^students/$', StudentCreateView.as_view(), name='students'),
    url(r'^students/(?P<pk>[0-9]+)$', StudentDetailView.as_view(), name='detail'),
    path('rest-auth/', include('rest_auth.urls'))
]