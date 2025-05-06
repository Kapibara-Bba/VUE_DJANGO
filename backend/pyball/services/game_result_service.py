from ..models import Team, GameResult


def insertGameResult(req):
  """試合結果登録"""
  GameResult.objects.create(
    team_id=req['team_id'],
    date=req['game_date'],
    opponent=req['opponent'],
    my_team_score=req['my_team_score'],
    opponent_score=req['opponent_score'],
    winning_pitcher=req['winning_pitcher'],
    losing_pitcher=req['losing_pitcher'],
    save_pitcher=req['save_pitcher'],
    home_run=req['home_run'],
    notes=req['notes'],
  )


def fetchGameResults(team_id):
  """試合結果一覧取得"""
  game_results = GameResult.objects.filter(team_id=team_id)

  game_result_list = []

  for game_result in game_results:
    game_result_list.append({
      "game_result_id": game_result.id,
      "game_date": game_result.date,
      "opponent": game_result.opponent,
      "my_team_score": game_result.my_team_score,
      "opponent_score": game_result.opponent_score,
      "winning_pitcher": game_result.winning_pitcher,
      "losing_pitcher": game_result.losing_pitcher,
      "save_pitcher": game_result.save_pitcher,
      "home_run": game_result.home_run,
      "notes": game_result.notes,
    })

  return game_result_list

def updateGameResult(req):
  """試合結果更新"""
  GameResult.objects.filter(id=req['game_result_id']).update(
    date=req['game_date'],
    opponent=req['opponent'],
    my_team_score=req['my_team_score'],
    opponent_score=req['opponent_score'],
    winning_pitcher=req['winning_pitcher'],
    losing_pitcher=req['losing_pitcher'],
    save_pitcher=req['save_pitcher'],
    home_run=req['home_run'],
    notes=req['notes']
  )

def deleteGameResult(game_result_id):
  """試合結果削除"""
  GameResult.objects.filter(id=game_result_id).delete()