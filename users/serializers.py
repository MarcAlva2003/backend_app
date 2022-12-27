from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'last_name', 'first_name', 'email', 'date_joined')
    # fields = '__all__'

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            # 'last_name',
            # 'first_name'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            # validated_data['last_name'],
            # validated_data['first_name'],
            validated_data['password']
        )

        return user