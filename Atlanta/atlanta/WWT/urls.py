from django.urls import path
from .views import *
from order.models import *

urlpatterns = [
    path('', wwt_def, name='home_page'),
    path('main/', thank_after_form, name='thank_after_form'),
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]
