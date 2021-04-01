from .views import *

from django.urls import path
app_name = 'book'

urlpatterns =[

    path('bot/<str:query>/', ChatBOT.as_view(), name="chatbot")
    ]