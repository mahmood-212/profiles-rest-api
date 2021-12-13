from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


# from django.shortcuts import render

# # Create your views here.

class HelloApiView(APIView):
    '''Test API '''
    serializer_class = serializers.HelloSerializer
    

    def get(self, request, format=None):

        an_apiview = [
            'mahmood',
            'ali',
            'Basunbul',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self,request):
        '''create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            print(f"{name}")

            message = f"Hello {name}"

            return Response({
                'message':message,

            })
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        '''Handle update an object'''
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        '''Handle partial update of an object'''
        return Response({'methond':'Patch'})

    def delete(self, request, pk=None):
        '''Delete an object '''
        return Response({'method':'Delete'})



