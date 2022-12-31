from django.urls import path, include
from rest_framework import routers
from .views import AboutView, SkillsViewSet, WorksViewSet

router = routers.DefaultRouter()

router.register(r'skills', SkillsViewSet, basename='skills')
router.register(r'works', WorksViewSet, basename='works')

urlpatterns = [
    path('about/<int:pk>/', AboutView.as_view(), name='about'),
    path('', include(router.urls))
]


