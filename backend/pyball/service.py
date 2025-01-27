from .models import Member


def createMember(member_name, password, team):
  Member.objects.create(
    team=team,
    name=member_name,
    password=password
  )