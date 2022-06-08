from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views
from . import utils

# Create your views here.

class UnicodeTranslatorView(views.APIView):
    def get(self, request, *args, **kwargs):
        input = request.query_params['input']
        return Response({
            'circled': utils.generate_circled(input),
            'fullwidth': utils.generate_fullwidth(input)
        })
