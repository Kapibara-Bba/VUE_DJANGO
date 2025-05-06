from ..models import Schedule, Team


def insertSchedule(req):
  """スケジュール登録"""
  return Schedule.objects.create(
    schedule_name=req['schedule_name'],
    team=Team.objects.get(id=req['team_id']),
    plan_date=req['plan_date'],
    notes=req['notes']
  )

def fetchSchedules(team_id):
  """スケジュール取得"""
  schedules = Schedule.objects.filter(team_id=team_id)

  schedule_list = []

  for schedule in schedules:
    schedule_list.append({
      "schedule_id": schedule.id,
      "schedule_name": schedule.schedule_name,
      "plan_date": schedule.plan_date,
      "notes": schedule.notes
    })

  return schedule_list

def updateSchedule(schedule_id, req):
  """スケジュール更新"""
  Schedule.objects.filter(id=schedule_id).update(
    schedule_name=req['schedule_name'],
    plan_date=req['plan_date'],
    notes=req['notes']
  )

def deleteSchedule(schedule_id):
  """スケジュール削除"""
  Schedule.objects.filter(id=schedule_id).delete()