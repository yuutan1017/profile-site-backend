from django.urls import path, include
from rest_framework import routers
from .views import AboutView, DetailViewSet, DescriptionView, WorksViewSet

router = routers.DefaultRouter()

router.register(r'skills', DetailViewSet, basename='skills')
router.register(r'works', WorksViewSet, basename='works')

urlpatterns = [
    path('about/<int:pk>/', AboutView.as_view(), name='about'),
    path('description/<int:pk>/', DescriptionView.as_view(), name='skill_description'),
    path('', include(router.urls))
]


