from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})



class HelloViewSets(viewsets.ViewSet):
    """ defining viewset class of our operations """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ retive list of object for now display list"""
        an_viewset = ["this is a Viewset",
         "lets try the basics",
         "ok end",
         ]
        return Response({'message':'Hello Viewsets', 'list': an_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle creating and updating profile"""
    serializer_class =serializers.UserProfileSerializer
    queryset =models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
