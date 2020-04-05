from django.shortcuts import render
from django.http import HttpResponse

from .models import List

# Create your views here.

def index(request):
    todo_list = List.object.all()

    context = {'todo_list':todo_list}
    return render(request, 'todo_list/home.html', context)