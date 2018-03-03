from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, GetView


urlpatterns = {
    url(r'^get/$', GetView.as_view(), name="get"),
    url(r'^sale/$', CreateView.as_view(), name="create"),
    url(r'^sale/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)