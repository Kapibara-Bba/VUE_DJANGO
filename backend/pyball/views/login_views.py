import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Member
from ..serializers import LoginSerializer, RegisterSerializer
from ..services.login_service import createMember, fetchTeam, createTeam, checkMember
from django.forms.models import model_to_dict
from ..services.team_service import fetchTeamInfo

logger = logging.getLogger(__name__)

class LoginView(APIView):
  """ログイン処理"""
  def post(self, request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
      username = serializer.validated_data['name']
      password = serializer.validated_data['password']
      user = checkMember(username=username, password=password)
      print(user)
      if user:
        # ユーザが存在した場合、チーム情報も取得
        team = fetchTeamInfo(user["team_id"])
        res = {
          "user": user,
          "team": team
        }
        return Response(data=res, status=200)
      return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
  def get(self, request):
    """チーム情報取得"""
    team_list = fetchTeam()
    return Response(data=team_list, status=200)

  def post(self, request):
    """メンバー新規登録"""
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data['name']
      password = serializer.validated_data['password']
      team_id = serializer.validated_data['team_id']
      team_name = serializer.validated_data['team_name']
      director = serializer.validated_data['director']

      if team_id is None:
        # チーム登録
        team = createTeam(team_name=team_name, director=director)
        team_id=team.id

      # メンバー登録
      create_data = model_to_dict(createMember(member_name=name, password=password, team_id=team_id))
      
      # チーム情報取得
      team = fetchTeamInfo(create_data["team"])

      res = {
          "user": create_data,
          "team": team
        }
      return Response(data=res, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)