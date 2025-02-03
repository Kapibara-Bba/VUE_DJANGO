from .models import Member, Team

def fetchTeam():
  """メンバー新規登録時のチーム情報取得"""
  return Team.objects.all().values_list("id", "name", "director")

def fetchOrCreateTeam(team_id, team_name, director):
  """チーム検索・登録"""
  if team_id:
    team = Team.objects.filter(id=team_id)
    if not team:
      return Team.objects.create(
        team_name=team_name,
        director=director
      )

def createMember(member_name, password, team_id):
  """メンバー登録"""
  print("★★★★Service★★★★★")
  print(member_name)
  print(password)
  print(team_id)
  Member.objects.create(
    team=team_id,
    name=member_name,
    password=password
  )