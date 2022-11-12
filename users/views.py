from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer, HJTokenObtainPairSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"회원가입 성공~!"}, status=status.HTTP_201_CREATED)
        return Response({"message":"회원가입 실패~!"}, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = HJTokenObtainPairSerializer