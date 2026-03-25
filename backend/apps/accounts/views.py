from django.http import request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


# 🔹 Register
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response(
            {
                "message": "User created successfully",
                "username": user.username
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        {"errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )


# 🔹 Protected route
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    return Response({"msg": "You are authenticated",
    "user": str(request.user),
        "auth": str(request.auth)})

        
@api_view(['GET'])
def hello(request):
    return Response({"msg": "hi"})