from .models import Member, Team

def fetchTeam():
  return Team.objects.all()

def createMember(member_name, password, team):
  print("★★★★Service★★★★★")
  print(member_name)
  print(password)
  print(team)
  Member.objects.create(
    team=team,
    name=member_name,
    password=password
  )