from django.db.models import Count
from django.shortcuts import render
from .models import *


def brands(request):
    posts = Brand.objects.all().annotate(count=models.Count('notebooks')).order_by('-count').filter(count__gt=0)    # exclude(count=False)
    context = {'brands': posts}
    return render(request, 'notebooks/index.html', context)


def home(request):
    context = {
        'home': 'yes',
    }
    return render(request, 'notebooks/index.html', context)


def notebooks(request):
    books = Notebook.objects.values('height', 'width', 'depth').\
        annotate(height_n=Count('height')).annotate(width_n=Count('width')).\
        annotate(depth_n=Count('depth')).\
        annotate(count_n=Count('brand_id')).order_by('width')
    
    # books = Notebook.objects.values('height').annotate(height_n=Count('height')).filter(height_n__gt=0)
    context = {'notebooks': books}
    return render(request, 'notebooks/index.html', context)


def round_to0and5():
    books = Notebook.objects.all()
    for el in books:
        w = round(el.width/10 * 2) / 2 * 10
        d = round(el.depth/10 * 2) / 2 * 10
        h = round(el.height/10 * 2) / 2 * 10
        el.height = h
        el.width = w
        el.depth = d
        el.save()
    return 'completed'
