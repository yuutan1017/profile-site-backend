from rest_framework import serializers
from api.models import About, Skills, Works


class AboutSerializer(serializers.ModelSerializer):
  class Meta:
    model = About
    fields = ('id', 'image')


class SkillsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skills
    fields = ('id', 'title', 'color_code')


class WorksSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

  class Meta:
    model = Works
    fields = ('id', 'image', 'title', 'description', 'url', 'created_at')
    
