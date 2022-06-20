
from django.urls import path
from .views import *
 
urlpatterns = [
    path('', CallbackDetailView.as_view(), name='callback'),
    path('', CallbackDetailView.as_view(), name='success'),
]