from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context = {
    'name': 'Jane Doe',
    'age': 23,
    'nationality': 'British'
  }
  return render(request, 'index.html', context)

def counter(request):
  text = request.POST['text']
  amountOfWords = len(text.split())
  return render(
    request, 'counter.html', { 'amountOfWords': amountOfWords })