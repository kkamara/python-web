from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
  features = Feature.objects.all()
  context = { 'features': features}
  return render(request, 'index.html', context)

def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email already exists.')
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username already exists.')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email,password=password)
        user.save()
        return redirect('login')
  return render(request, 'register.html')

def counter(request):
  text = request.POST['text']
  amountOfWords = len(text.split())
  return render(
    request, 'counter.html', { 'amountOfWords': amountOfWords })