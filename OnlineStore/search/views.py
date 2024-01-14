from django.shortcuts import render
from store.forms import ProductSearchForm
from store.models import Item

def search(request):
    form = ProductSearchForm(request.GET)
    items = []
    if form.is_valid():
        search_term = form.cleaned_data['search_term']
        items = Item.objects.filter(title__icontains=search_term)
    return render(request, 'search/search_results.html', {'form': form, 'items': items})
