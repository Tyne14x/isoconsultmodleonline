from django.shortcuts import render
from app_users.forms import RegisterFrom

# Create your views here.

def register(request):
form = RegisterFrom()
context = {"form=form"}
return render(request, "app_users/register.html", context)
