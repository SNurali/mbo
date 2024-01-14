# context_processors.py
from .models import ItemTag

def categories(request):
    return {'categories': ItemTag.objects.all()}