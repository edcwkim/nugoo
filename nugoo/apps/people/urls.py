from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^p/', include([
        url(r'(?P<pk>\d+)/', include([
            url(r'^$', views.PersonDetail.as_view(), name='person-detail'),
        ])),
    ])),
]
