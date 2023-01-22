from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'app_general/home.html')


def contact(request):
    return render(request, 'app_general/contact.html')


def blog(request):
    return render(request, 'app_general/blog.html')


def news(request):
    return render(request, 'app_general/news.html')


def eiearning(request):
    return render(request, 'app_general/eiearning.html')


def training(request):
    return render(request, 'app_general/training.html')


def published_documents(request):
    return render(request, 'app_general/published_documents.html')


def course(request):
    return render(request, 'app_general/course.html')


def introduction_video(request):
    return render(request, 'app_general/introduction_video.html')
