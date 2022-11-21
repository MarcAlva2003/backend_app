from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions, generics
from knox.models import AuthToken

class UserInformation(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })