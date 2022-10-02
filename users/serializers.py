from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'last_name', 'last_name', 'email', 'date_joined']