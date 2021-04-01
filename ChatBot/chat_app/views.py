from django.shortcuts import render

from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
# from

from django.db.models import F
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from . chatter_bot import chatbot
import json


class ChatBOT(APIView):
    def get(self, request, *args, **kwargs):
        try:
            question = kwargs.get('query')
            data = chatbot.get_response(question)
            return JsonResponse({'results': str(data)})
        except:
            return status.HTTP_422_UNPROCESSABLE_ENTITY
