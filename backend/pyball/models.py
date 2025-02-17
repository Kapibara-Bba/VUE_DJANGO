from django.db import models


class Team(models.Model):
  team_name = models.CharField(max_length=100, null=False)
  director = models.CharField(max_length=100, null=False)
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField(max_length=100, null=True)
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField(max_length=100, null=True)

class Member(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=False)
  password = models.CharField(max_length=20, null=False)
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField(max_length=100, null=True)
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField(max_length=100, null=True)

class Schedule(models.Model):
  schedule_name = models.CharField(max_length=100, null=True)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
  plan_date = models.DateField(null=True)
  notes = models.CharField(max_length=300, null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField(max_length=100, null=True)
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField(max_length=100, null=True)

class GameResult(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
  date = models.DateField(null=True)
  opponent = models.CharField(max_length=100, null=True)
  my_team_score = models.IntegerField()
  opponent_score = models.IntegerField()
  winning_pitcher = models.CharField(max_length=100, null=True)
  losing_pitcher = models.CharField(max_length=100, null=True)
  save_pitcher = models.CharField(max_length=100, null=True)
  home_run = models.CharField(max_length=100, null=True)
  notes = models.CharField(max_length=300, null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField(max_length=100, null=True)
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField(max_length=100, null=True)
