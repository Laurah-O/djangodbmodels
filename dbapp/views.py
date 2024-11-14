from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import GeeksModel

def index(request):
    try:
        items = GeeksModel.objects.all()
    except GeeksModel.DoesNotExist:
        raise Http404("No items found")
    return render(request, 'index.html', {'items': items})

def detail(request, id):
    item = get_object_or_404(GeeksModel, pk=id)
    return render(request, 'detail.html', {'item': item})