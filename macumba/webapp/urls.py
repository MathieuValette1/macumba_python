from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('uploads', uploads, name="uploads"),
    path('reno', reno, name="reno")
]