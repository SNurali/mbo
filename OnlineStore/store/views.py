from django.shortcuts import get_object_or_404, render

from .models import Item, ItemTag
from .paginator import paginator
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ProductSearchForm



def store(request):
    items = Item.objects.filter(is_available=True)
    tags = ItemTag.objects.all()
    form = ProductSearchForm()  # Create an instance of the form here
    context = {
        'page_obj': paginator(request, items, 9),
        'range': [*range(1, 7)],
        'tags': tags,
        'form': form,  # Pass the form to the template context
    }

    return render(request, 'store/main_page.html', context)



def item_details(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'store/item_details.html', context)


def tag_details(request, slug):
    tag = get_object_or_404(ItemTag, slug=slug)
    items = Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'page_obj': paginator(request, items, 3),
    }
    return render(request, 'store/tag_details.html', context)


def tag_list(request):
    tags = ItemTag.objects.all()
    context = {
        'page_obj': paginator(request, tags, 6),
        'tags':tags
    }
    return render(request, 'store/tag_list.html', context)

def tag_details_redirect(request):
    slug = request.GET.get('slug')
    return redirect('store:tag_details', slug=slug)
def items_by_category(request):
    slug = request.GET.get('slug')
    category = get_object_or_404(ItemTag, slug=slug)
    items = Item.objects.filter(tags__in=[category])
    return render(request, 'store/items_by_category.html', {'items': items})


def search_results(request):
    form = ProductSearchForm(request.GET)
    items = Item.objects.all()
    if 'search_term' in request.GET and request.GET['search_term']:
        search_term = request.GET['search_term']
        items = items.filter(title__icontains=search_term)

    if 'category' in request.GET and request.GET['category']:
        category_id = request.GET['category']
        items = items.filter(tags__id=category_id)

    context = {
        'form': form,
        'items': items,
    }
    return render(request, 'store/search_results.html', context)

