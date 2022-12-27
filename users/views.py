from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions, generics, authtoken
# from knox.models import AuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def checkUsernameExists(requestUsername):
  user = User.objects.filter(username = requestUsername)
  return len(user) > 0

class UserInformation(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
  
  permission_classes = [permissions.IsAuthenticated]
  def put(self, request, *args, **kwargs):
    user = User.objects.filter(username = request.user.username).first()
    data = request.data
    print('------------')
    print(user.username)
    print('------------')
    # print(request.data['operation'])
    # CHANGE USERNAME

    if data['operation'] == 'username':
      # CHECK USERNAME IN USE
      if checkUsernameExists(request.data['username']):
        return Response({"Fail": "Error: username already taken"}, status=status.HTTP_200_OK)
      else:
        user.username = data['username']
        user.save()
        return Response({"Success": "Succes: username changed successfuly"}, status=status.HTTP_200_OK)
    
    elif data['operation'] == 'first_name':
      try:
        user.first_name = data['first_name']
        user.save()
      except KeyError:
        return Response({"Error": "First name is requiered"}, status=status.HTTP_400_BAD_REQUEST)
      return Response({"Success": "Succes: first name changed successfuly"}, status=status.HTTP_200_OK)
    
    elif data['operation'] == 'last_name':
      try:
        user.last_name = data['last_name']
        user.save()
      except KeyError:
        return Response({"Error": "Last name is requiered"}, status=status.HTTP_400_BAD_REQUEST)
      return Response({"Success": "Succes: last name changed successfuly"}, status=status.HTTP_200_OK)
    else:
      return Response({"Error": "Error: invalid operation"}, status=status.HTTP_400_BAD_REQUEST )
      

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        print('-----------------------')
        print(token)
        print(serializer.is_valid(raise_exception=True))
        print(UserSerializer(user, context=self.get_serializer_context()).data)
        return Response({
          "user": UserSerializer(user, context=self.get_serializer_context()).data,
          "token": str(token)
        })