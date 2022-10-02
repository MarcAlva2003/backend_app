from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer



# Create your views here.
@api_view(['get'])
def user_view_get(request):
  serializer = UserSerializer(request.user)
  return Response(serializer.data)