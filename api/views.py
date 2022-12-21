from rest_framework import generics, viewsets, mixins
from .serializers import AboutSerializer, SkillsSerializer, WorksSerializer
from .models import About, Skills, Works


class AboutView(generics.ListAPIView):
  queryset = About.objects.all()
  serializer_class = AboutSerializer

  # def get(self, request, *args, **kwargs):
  #   return self.list(request, *args, **kwargs) 

  # def put(self, request, *args, **kwargs):
  #   return self.update(request, *args, **kwargs)


class SkillsView(generics.ListAPIView):
  queryset = Skills.objects.all()
  serializer_class = SkillsSerializer


class SkillDetailView(generics.RetrieveAPIView):
  queryset = Skills.objects.all()
  serializer_class = SkillsSerializer


class WorksView(generics.ListAPIView):
  queryset = Works.objects.all()
  serializer_class = WorksSerializer


class WorkDetailView(generics.RetrieveAPIView):
  queryset = Works.objects.all()
  serializer_class = WorksSerializer

