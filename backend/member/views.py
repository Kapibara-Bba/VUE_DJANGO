from django.views import View
from pyball.models import Member
from django.shortcuts import render
from .serializers import MemberSerializer

# Create your views here.
class LoginViews(View):
  member = Member.objects.all()
  member_serializer = MemberSerializer