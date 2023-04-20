from django.shortcuts import render, get_object_or_404
from .models import *

def notes_home(request):
    return render(request, 'notes_home.html')

def category_info(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    return render(request, 'catinfo.html', {'category':category})

# Create your views here.
