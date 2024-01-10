from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Manvi', 'place':'India'}
    return render(request,'task.html',params)