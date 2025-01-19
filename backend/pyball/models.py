from django.db import models


class Member(models.Model):
  team = models.ForeignKey
  name = models.CharField(max_length=100)
  password = models.CharField
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField

class Team(models.Model):
  schedule = models.ForeignKey
  game_result = models.ForeignKey
  name = models.CharField
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField

class Schedule(models.Model):
  name = models.CharField
  plan_date = models.DateField
  notes = models.CharField
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField

class GameResult(models.Model):
  date = models.DateField
  opponent = models.CharField
  my_team_score = models.IntegerField
  opponent_score = models.IntegerField
  winning_pitcher = models.CharField
  losing_pitcher = models.CharField
  save_pitcher = models.CharField
  home_run = models.CharField
  notes = models.CharField
  created_date = models.DateTimeField(auto_now_add=True)
  created_user = models.CharField
  updated_date = models.DateTimeField(auto_now_add=True)
  updated_user = models.CharField
