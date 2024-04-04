from django.shortcuts import render, redirect
from . forms import CategoryModel
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = CategoryModel(request.POST)
        if category_form.is_valid():
            category_form.save()
            redirect('add_category')
    else:
        category_form = CategoryModel()
    return render(request, 'add_category.html', {'form': category_form})
