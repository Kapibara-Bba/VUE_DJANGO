from rest_framework import views
from ..models import Member
from django.shortcuts import render
from .serializers import MemberSerializer

# Create your views here.
class LoginViews(views):
  member = Member.objects.all()
  member_serializer = MemberSerializer