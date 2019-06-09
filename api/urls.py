from django.conf.urls import url, include
from django.urls import path

from api.views import StudentListView, StudentDetailView, StudentCreateView

urlpatterns = [
    url(r'^students/view/$', StudentListView.as_view(), name='view'),
    url(r'^students/add/$', StudentCreateView.as_view(), name='add'),
    url(r'^students/$', StudentListView.as_view(), name='students'),
    url(r'^students/(?P<pk>[0-9]+)$', StudentDetailView.as_view(), name='detail'),
    path('rest-auth/', include('rest_auth.urls'))
]