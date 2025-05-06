from ..models import Member, Team
from django.forms.models import model_to_dict

def checkMember(username, password):
  """ログイン時のユーザ検索"""
  return Member.objects.filter(name=username, password=password).values().first()

def fetchTeam():
  """メンバー新規登録時のチーム情報取得"""
  return [model_to_dict(team) for team in Team.objects.all()]

def createTeam(team_name, director):
  """チーム登録"""
  return Team.objects.create(
    team_name=team_name,
    director=director
  )

def createMember(member_name, password, team_id):
  """メンバー登録"""
  return Member.objects.create(
    team=Team.objects.get(id=team_id),
    name=member_name,
    password=password
  )