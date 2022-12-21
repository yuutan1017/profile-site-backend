from django.urls import path, include
from api import views

from rest_framework import routers
from .views import AboutViewSet, SkillsViewSet, WorksViewSet

router = routers.DefaultRouter()

router.register(r'about', AboutViewSet, basename='about')
router.register(r'skills', SkillsViewSet, basename='skills')
router.register(r'works', WorksViewSet, basename='works')

urlpatterns = router.urls

