from django.urls import path

from .views import item_details, store, tag_details, tag_list, items_by_category, tag_details_redirect, search_results

app_name = 'store'

urlpatterns = [
    path('', store, name='home'),
    path('categories/', tag_list, name='tag_list'),
    path('category-details/<slug:slug>/', tag_details, name='tag_details'),
    path('items_by_category/', items_by_category, name='items_by_category'),
    path('tag_details_redirect/', tag_details_redirect, name='tag_details_redirect'),
    path('search_results/', search_results, name='search_results'),
    path('<slug:item_slug>/', item_details, name='item_details'),
]