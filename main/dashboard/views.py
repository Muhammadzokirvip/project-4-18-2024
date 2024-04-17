from django.shortcuts import render, redirect
from .models import Category
from django.http import Http404

def get_category(pk):
    try:
        return Category.objects.get(pk=pk)
    except Category.Topilmadi:
        raise Http404("Category does not exist")

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})  

def category_detail(request, pk):
    category = get_category(pk)
    return render(request, 'categories/detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
#create
     return render(request, 'categories/create.html')

def category_update(request, pk):
    category = get_category(pk) 
    if request.method == 'POST':
# update
     return render(request, 'categories/update.html', {'category': category})  

def category_delete(request, pk):
    category = get_category(pk)
    if request.method == 'POST':
#delete
     return render(request, 'categories/delete.html', {'category': category})
