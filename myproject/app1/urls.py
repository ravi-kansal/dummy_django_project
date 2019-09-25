from django.urls import path
from .views import *

urlpatterns = [
    path('',Dummy.as_view(),name='dummy')
]