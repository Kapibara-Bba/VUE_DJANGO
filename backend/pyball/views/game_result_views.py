from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers import GameResultSerializer
from ..services.game_result_service import fetchGameResults, insertGameResult, updateGameResult, deleteGameResult


class GameResultView(APIView):
  """試合結果"""

  def get(self, request, team_id, *args, **kwargs):
    """試合結果一覧取得"""
    team_id = self.kwargs.get('team_id')
    data = fetchGameResults(team_id=team_id)

    return Response(data=data, status=200)

  def post(self, request, team_id, *args, **kwargs):
    """試合結果登録"""
    team_id = self.kwargs.get('team_id')
    serializer = GameResultSerializer(data=request.data)
    if serializer.is_valid():
      req_dict = {
        "team_id": team_id,
        "game_date": serializer.validated_data["game_date"],
        "opponent": serializer._validated_data["opponent"],
        "my_team_score": serializer.validated_data["my_team_score"],
        "opponent_score": serializer.validated_data["opponent_score"],
        "winning_pitcher": serializer._validated_data["winning_pitcher"],
        "losing_pitcher": serializer.validated_data["losing_pitcher"],
        "save_pitcher": serializer.validated_data["save_pitcher"],
        "home_run": serializer._validated_data["home_run"],
        "notes": serializer.validated_data["notes"]
      }

      insertGameResult(req=req_dict)
      return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, team_id, game_result_id, *args, **kwargs):
    """試合結果更新"""
    serializer = GameResultSerializer(data=request.data)
    if serializer.is_valid():
      req_dict = {
        "game_result_id": game_result_id,
        "team_id": team_id,
        "game_date": serializer.validated_data["game_date"],
        "opponent": serializer._validated_data["opponent"],
        "my_team_score": serializer.validated_data["my_team_score"],
        "opponent_score": serializer.validated_data["opponent_score"],
        "winning_pitcher": serializer._validated_data["winning_pitcher"],
        "losing_pitcher": serializer.validated_data["losing_pitcher"],
        "save_pitcher": serializer.validated_data["save_pitcher"],
        "home_run": serializer._validated_data["home_run"],
        "notes": serializer.validated_data["notes"]
      }
      updateGameResult(req=req_dict)
      return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, team_id, game_result_id, *args, **kwargs):
    """試合結果削除"""
    deleteGameResult(game_result_id=game_result_id)

    return Response(status=status.HTTP_200_OK)
