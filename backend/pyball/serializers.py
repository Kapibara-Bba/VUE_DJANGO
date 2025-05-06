from rest_framework import serializers
from .models import Member, Team, Schedule, GameResult


class LoginSerializer(serializers.Serializer):
    """ログインシリアライザ"""
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class RegisterSerializer(serializers.Serializer):
    """ユーザ新規登録シリアライザ"""
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    team_id = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    team_name = serializers.CharField(required=True)
    director = serializers.CharField(required=True)

class ScheduleSerializer(serializers.Serializer):
    """スケジュール登録シリアライザ"""
    schedule_name = serializers.CharField(required=True)
    plan_date = serializers.DateField(required=True)
    notes = serializers.CharField(required= False, allow_null=True, allow_blank=True)

class GameResultSerializer(serializers.Serializer):
    """試合結果登録シリアライザ"""
    game_date = serializers.DateField(required=True)
    opponent = serializers.CharField(required=True)
    my_team_score = serializers.IntegerField(required=True)
    opponent_score = serializers.IntegerField(required=True)
    winning_pitcher = serializers.CharField(required= False, allow_null=True, allow_blank=True)
    losing_pitcher = serializers.CharField(required= False, allow_null=True, allow_blank=True)
    save_pitcher = serializers.CharField(required= False, allow_null=True, allow_blank=True)
    home_run = serializers.CharField(required= False, allow_null=True, allow_blank=True)
    notes = serializers.CharField(required= False, allow_null=True, allow_blank=True)

# class MemberSerializer(serializers.ModelSerializer):
#   """メンバーシリアライザ"""
#   class Meta:
#     model = Member
#     fields = '__all__'

# class TeamSerializer(serializers.ModelSerializer):
#   """チームシリアライザ"""
#   class Meta:
#     model = Team
#     fields = '__all__'

# class ScheduleSerializer(serializers.ModelSerializer):
#   """スケジュールシリアライザ"""
#   class Meta:
#     model = Schedule
#     fields = '__all__'

# class GameResultSerializer(serializers.ModelSerializer):
#   """試合結果シリアライザ"""
#   class Meta:
#     model = GameResult
#     fields = '__all__'
