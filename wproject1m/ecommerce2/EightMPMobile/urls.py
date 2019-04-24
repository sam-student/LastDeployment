
from django.urls import path
from django.conf.urls import url

from .views import \
    (
    ProductListView,\
    ProductDetailSlugView,
    EightMP_Mobile_upload,
     )

urlpatterns = [
    url(r'^$',ProductListView.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name="detail"),

]
