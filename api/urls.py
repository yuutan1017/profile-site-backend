from django.urls import path, include
from api import views

from rest_framework import routers
from .views import AboutViewSet

router = routers.DefaultRouter()

router.register(r'about', AboutViewSet, basename='about')

urlpatterns = [
    path('', include(router.urls)),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('skills/<str:pk>/', views.SkillDetailView.as_view(), name='skill-detail'),
    path('works/', views.WorksView.as_view(), name='works'),
    path('works/<str:pk>/', views.WorkDetailView.as_view(), name='work-detail'),
]

