from django.urls import path
from .views import *

urlpatterns=[
    path('hv/',hview),
    path('fv/',fview),
    path('sv/',sview)
]