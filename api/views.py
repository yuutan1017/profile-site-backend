from rest_framework import viewsets, generics
from .serializers import AboutSerializer, DetailSerializer,DescriptionSerializer, WorkSerializer
from .models import About, Skill_Detail, Skill_Description, Work


class AboutView(generics.RetrieveUpdateAPIView):
  queryset = About.objects.all()
  serializer_class = AboutSerializer


class DetailViewSet(viewsets.ModelViewSet):
  queryset = Skill_Detail.objects.all()
  serializer_class = DetailSerializer


class DescriptionView(viewsets.ModelViewSet):
  queryset = Skill_Description.objects.all()
  serializer_class = DescriptionSerializer


class WorksViewSet(viewsets.ModelViewSet):
  queryset = Work.objects.all()
  serializer_class = WorkSerializer


