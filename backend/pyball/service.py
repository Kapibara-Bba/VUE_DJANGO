from .models import Member, Team

def fetchTeam():
  """メンバー新規登録時のチーム情報取得"""
  return Team.objects.all().values_list("id", "name", "director")

def createTeam(team_name, director):
  """チーム登録"""
  print("★★★TeamCreate★★★")
  print(team_name)
  print(director)
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
    team=Team.objects.get(id=team_id),
    name=member_name,
    password=password
  )