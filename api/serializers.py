from rest_framework import serializers
from api.models import About, Skills, Works


class AboutSerializer(serializers.ModelSerializer):
  class Meta:
    model = About


class SkillsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skills


class WorksSerializer(serializers.ModelSerializer):
  class Meta:
    model = Works

    
