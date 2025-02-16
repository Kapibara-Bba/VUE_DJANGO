import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Member
from .serializers import LoginSerializer
from .service import createMember, fetchTeam, createTeam

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

class RegisterView(APIView):
  def get(self, request):
    """チーム情報取得"""
    print("★★★★get_member★★★★")
    team = fetchTeam
    Response(team)

  def post(self, request):
    """メンバー新規登録"""
    logger.debug("★★★★★★★")
    logger.info(f"Received data: {request.data}")
    print("★★★★★★★")
    print(f"Received data: {request.data}")
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data['name']
      password = serializer.validated_data['password']
      team_id = serializer.validated_data['team_id']
      team_name = serializer.validated_data['team_name']
      director = serializer.validated_data['director']

      if team_id is None:
        # チーム登録
        team = createTeam(team_name=team_name, director=director)
        print("TEAM_CERATED")
        print(team)
        print(team.id)
        team_id=team.id

      # メンバー登録
      print("TEAM_ID")
      print(team_id)
      print("TEAM_ID END")
      createMember(member_name=name, password=password, team_id=team_id)
      return Response({"message": "Register successful!"})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)