from django.urls import path
from app_general import views
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('news/', views.news, name='news'),
    path('eiearning/', views.eiearning, name='eiearning'),
    path('training/', views.training, name='training'),
    path('published_documents/', views.published_documents,name='published_documents'),
    path('course/', views.course, name='course'),
    path('introduction_video/', views.introduction_video, name='introduction_video'),
    path('register/', views.Register, name='register'),
]