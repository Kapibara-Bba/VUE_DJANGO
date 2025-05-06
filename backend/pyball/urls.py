from django.urls import path, include
from .views.login_views import LoginView, RegisterView
from .views.team_views import TeamsView
from .views.schedules_views import ScheduleView
from .views.game_result_views import GameResultView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('team/<int:id>/', TeamsView.as_view(), name='get_team'),
    path('<int:team_id>/schedules/', ScheduleView.as_view(), name='schedule'),
    path('<int:team_id>/schedules/<int:schedule_id>/', ScheduleView.as_view(), name='schedule-detail'),
    path('<int:team_id>/game-result/', GameResultView.as_view(), name='game-result'),
    path('<int:team_id>/game-result/<int:game_result_id>/', GameResultView.as_view(), name='game-result-detail'),
]