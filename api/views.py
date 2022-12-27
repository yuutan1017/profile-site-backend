from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import AboutSerializer, SkillSerializer, WorkSerializer
from .models import About, Skill, Work


class AboutViewSet(viewsets.ModelViewSet):
  queryset = About.objects.all()
  serializer_class = AboutSerializer

  def perform_create(self, serializer):
    serializer.save(image=self.request.image)


class SkillsViewSet(viewsets.ModelViewSet):
  queryset = Skill.objects.all()
  serializer_class = SkillSerializer


class WorksViewSet(viewsets.ModelViewSet):
  queryset = Work.objects.all()
  serializer_class = WorkSerializer


