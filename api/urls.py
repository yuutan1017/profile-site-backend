from django.urls import path
from api import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('skills/<str:pk>/', views.SkillDetailView.as_view(), name='skill-detail'),
    path('works/', views.WorksView.as_view(), name='works'),
    path('works/<str:pk>/', views.WorkDetailView.as_view(), name='work-detail'),
]

