from rest_framework import serializers
from api.models import About, Skill, Work


class AboutSerializer(serializers.ModelSerializer):
  class Meta:
    model = About
    fields = ('id', 'image')


class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill
    fields = ('id', 'title', 'color_code')


class WorkSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

  class Meta:
    model = Work
    fields = ('id', 'image', 'title', 'description', 'url', 'created_at', 'updated_at')
    
