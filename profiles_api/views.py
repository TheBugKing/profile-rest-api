from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test for HelloApiView."""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features """

        an_apiview =[
        '1',
        '2',
        '3',
        '4',
        ]

        return Response({'message':'MY-FIRST-API','api':an_apiview, 'list': [1,2,3,4]})


    def post(self, request):
        "Create a Welcome messgae with our name"
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            "retrive name field from data"
            name = serializer.validated_data.get('name')
            message = f'Welcome {name} , The Great'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
