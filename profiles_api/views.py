from rest_framework.views import APIView
from rest_framework.response import Response


# from django.shortcuts import render

# # Create your views here.

class HelloApiView(APIView):
    def get(self, request, format=None):

        an_apiview = [
            'mahmood',
            'ali',
            'Basunbul',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})



