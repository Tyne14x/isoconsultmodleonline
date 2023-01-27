from django.urls import path
from app_student import views

urlpatterns = [
    path('code_student', views.code_student, name='code_student'),
]