from django.db.models import Count, F, Q, ExpressionWrapper, IntegerField, FloatField
from django.db.models.functions import Round
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
    # books = Notebook.objects.\
    #     values('height', 'width', 'depth').\
    #     annotate(height_n=Count('height')).\
    #     annotate(width_n=Count('width')).\
    #     annotate(depth_n=Count('depth')).\
    #     annotate(count_n=Count('brand_id')).\
    #     order_by('width')

    # аннотации для height_n, width_n и depth_n можно не использовать
    # books = Notebook.objects.values('height').annotate(height_n=Count('height')).filter(height_n__gt=0)

    books = Notebook.objects.\
        annotate(height_n=Round((F('height') + 2.49) / 5) * 5).\
        annotate(width_n=Round((F('width') + 2.49) / 5) * 5).\
        annotate(depth_n=Round((F('depth') + 2.49) / 5) * 5).\
        order_by('width_n', 'depth_n', 'height_n')

    books = books.values('height_n', 'width_n', 'depth_n').annotate(count_n=Count('brand_id'))

    context = {'notebooks': books}
    return render(request, 'notebooks/index.html', context)


# def round_to0and5():
#     books = Notebook.objects.all()
#     for el in books:
#         w = round(el.width / 5) * 5
#         d = round(el.depth / 5) * 5
#         h = round(el.height / 5) * 5
#         el.height = h
#         el.width = w
#         el.depth = d
#         el.save()
#     return 'completed'
#
# def round0to5(el):
#     el = float(el)
#     w = round(el.width/10 * 2) / 2 * 10
#     return w
