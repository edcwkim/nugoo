from django.conf.urls import include, url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^p/', include([
        url(r'^$', RedirectView.as_view(pattern_name='people:person-list', permanent=True)),
        url(r'(?P<pk>\d+)/', include([
            url(r'^$', views.PersonDetail.as_view(), name='person-detail'),
        ])),
        url(r'(?P<name>.+)/', views.PersonListByName.as_view(), name='person-list-by-name'),
    ])),
    url(r'^people/$', views.PersonList.as_view(), name='person-list'),
]
