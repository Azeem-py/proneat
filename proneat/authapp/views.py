from rest_framework import views, viewsets,status
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from knox.auth import AuthToken, TokenAuthentication
from .serializers import CreateUserSerializer


class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _,token = AuthToken.objects.create(user)
        content = {
            "user": str(user), "token": token
        }
        return Response(content)



class UserView(views.APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)