from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from rest_framework.views import APIView
from rest_framework import permissions


# Create your views here.
# @api_view(['get'])
# @permission_required([IsAuthenticated])
# def user_view_get(self, request):
#   serializer = UserSerializer(self, request.user)
#   return Response(serializer.data)

class UserInformation(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
