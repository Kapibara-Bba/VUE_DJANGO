from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers import ScheduleSerializer
from ..services.schedules_service import insertSchedule, fetchSchedules, updateSchedule, deleteSchedule


class ScheduleView(APIView):
  """スケジュール"""

  def post(self, request, team_id, *args, **kwargs):
    """スケジュール登録"""
    team_id = self.kwargs.get('team_id')
    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
      req_dict = {
        "schedule_name": serializer.validated_data["schedule_name"],
        "team_id": team_id,
        "plan_date": serializer.validated_data["plan_date"],
        "notes": serializer.validated_data["notes"]
      }

      insertSchedule(req=req_dict)
      return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, team_id, *args, **kwargs):
    """スケジュール検索"""
    team_id = self.kwargs.get('team_id')

    data = fetchSchedules(team_id=team_id)
    return Response(data=data, status=status.HTTP_200_OK)

  def put(self, request, team_id, schedule_id):
    """スケジュール更新"""

    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
      req_dict = {
        "schedule_name": serializer.validated_data["schedule_name"],
        "team_id": team_id,
        "plan_date": serializer.validated_data["plan_date"],
        "notes": serializer.validated_data["notes"]
      }
      updateSchedule(schedule_id=schedule_id, req=req_dict)
      return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, team_id, schedule_id):
    """スケジュール削除"""
    deleteSchedule(schedule_id=schedule_id)

    return Response(status=status.HTTP_200_OK)

