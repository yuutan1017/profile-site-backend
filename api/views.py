from rest_framework import viewsets
from .serializers import AboutSerializer, SkillsSerializer, WorksSerializer
from .models import About, Skills, Works


class AboutViewSet(viewsets.ModelViewSet):
  queryset = About.objects.all()
  serializer_class = AboutSerializer


class SkillsViewSet(viewsets.ModelViewSet):
  queryset = Skills.objects.all()
  serializer_class = SkillsSerializer


class WorksViewSet(viewsets.ModelViewSet):
  queryset = Works.objects.all()
  serializer_class = WorksSerializer


