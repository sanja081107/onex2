from .views import *
from django.urls import path


urlpatterns = [
    path('', home),
    path('brands/', brands, name='brands'),
    path('notebooks/', notebooks, name='notebooks'),
]
