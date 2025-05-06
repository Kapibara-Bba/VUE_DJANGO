from ..models import Team

def fetchTeamInfo(team_id):
  """チームに紐づく情報を取得する"""

  team = Team.objects.prefetch_related('member_set', 'schedule_set', 'gameresult_set').get(id=team_id)

  team_dict = {
      "team_name": team.team_name,
      "director": team.director,
      "members": [],
      "schedules": [],
      "gameresults": [],
  }

  for member in team.member_set.all():
    team_dict["members"].append({
      "name": member.name
    })

  for schedule in team.schedule_set.all():
    team_dict["schedules"].append({
      "schedule_id": schedule.id,
      "schedule_name": schedule.schedule_name,
      "plan_date": schedule.plan_date,
      "notes": schedule.notes
    })

  for game_result in team.gameresult_set.all():
    team_dict["gameresults"].append({
      "game_result_id": game_result.id,
      "game_date": game_result.date,
      "opponent": game_result.opponent,
      "my_team_score": game_result.my_team_score,
      "opponent_score": game_result.opponent_score,
      "winning_pitcher": game_result.winning_pitcher,
      "losing_pitcher": game_result.losing_pitcher,
      "save_pitcher": game_result.save_pitcher,
      "home_run": game_result.home_run,
      "notes": game_result.notes
    })
  return team_dict