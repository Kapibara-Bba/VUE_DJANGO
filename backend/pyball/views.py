from rest_framework import views
from .models import Member
from django.shortcuts import render
from .serializers import LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class LoginView(APIView):
    def post(self, request):
        logger.debug("★★★★★★★")
        logger.info(f"Received data: {request.data}")
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['name']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                return Response({"message": "Login successful!"})
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)