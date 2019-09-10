from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={}
    context['name'] = 'Ashwani'

    return render(request,'api/index.html', context=context)