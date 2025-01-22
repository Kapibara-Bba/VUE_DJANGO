from django.urls import path, include
from .views import LoginViews

urlpatterns = [
    path('login/', LoginViews.as_view()),
]