from rest_framework import viewsets
from .serializers import AboutSerializer, SkillSerializer, WorkSerializer
from .models import About, Skill, Work


class AboutViewSet(viewsets.ModelViewSet):
  queryset = About.objects.all()
  serializer_class = AboutSerializer


class SkillsViewSet(viewsets.ModelViewSet):
  queryset = Skill.objects.all()
  serializer_class = SkillSerializer


class WorksViewSet(viewsets.ModelViewSet):
  queryset = Work.objects.all()
  serializer_class = WorkSerializer


