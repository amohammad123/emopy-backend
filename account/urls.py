from django.urls import path
from .views import *

urlpatterns = [
    path('send-code/', SendCode.as_view()),
    path('check-code/', CheckCode.as_view()),
    path('detail/', UserDetails.as_view()),
]
