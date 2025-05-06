from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..services.team_service import fetchTeamInfo

class TeamsView(APIView):
  def get(self, request, id, *args, **kwargs):
    """ユーザ所属チーム情報取得"""

    team_dict = fetchTeamInfo(id)
    print(team_dict)
    return Response(data=team_dict, status=status.HTTP_200_OK)