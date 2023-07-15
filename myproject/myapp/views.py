from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
  feature1 = Feature()
  feature1.id = 0
  feature1.name = 'Fast'
  feature1.isTrue = True
  feature1.details = 'Our service is very quick.'

  feature2 = Feature()
  feature2.id = 1
  feature2.name = 'Reliable'
  feature2.isTrue = True
  feature2.details = 'Our service is very reliable.'

  feature3 = Feature()
  feature3.id = 2
  feature3.isTrue = False
  feature3.name = 'Easy To Use'
  feature3.details = 'Our service is easy to use.'

  feature4 = Feature()
  feature4.id = 3
  feature4.isTrue = True
  feature4.name = 'Affordable'
  feature4.details = 'Our service is very affordable.'

  features = [feature1, feature2, feature3, feature4]
  context = { 'features': features}
  return render(request, 'index.html', context)

def counter(request):
  text = request.POST['text']
  amountOfWords = len(text.split())
  return render(
    request, 'counter.html', { 'amountOfWords': amountOfWords })