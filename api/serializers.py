from rest_framework import serializers
from api.models import About, Skill_Detail, Skill_Description, Work


class AboutSerializer(serializers.ModelSerializer):
  class Meta:
    model = About
    fields = ('id', 'image', 'text')


class DetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill_Detail
    fields = ('id', 'category', 'title', 'color_code')


class DescriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill_Description
    fields = ('id', 'description')


class WorkSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

  class Meta:
    model = Work
    fields = ('id', 'image', 'title', 'description', 'url', 'created_at', 'updated_at')
    
