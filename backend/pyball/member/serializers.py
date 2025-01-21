from rest_framework import serializers
from ..models import Member, Team, Schedule, GameResult

class MemberSerializer(serializers.ModelSerializer):
  """メンバーシリアライザ"""
  class Meta:
    model = Member
    fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
  """チームシリアライザ"""
  class Meta:
    model = Team
    fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
  """スケジュールシリアライザ"""
  class Meta:
    model = Schedule
    fields = '__all__'

class GameResultSerializer(serializers.ModelSerializer):
  """試合結果シリアライザ"""
  class Meta:
    model = GameResult
    fields = '__all__'
