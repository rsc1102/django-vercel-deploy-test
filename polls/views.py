from django.shortcuts import render
from .models import ListItem
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse

# Create your views here.

def index(request):
    items = ListItem.objects.values_list('item', flat=True)
    context = {"items":items}
    return render(request, "polls/index.html" ,context)


@require_POST
def add_item(request):
    try:
        item = json.loads(request.body)['item']
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    new_item = ListItem(item=item)
    new_item.save()
    return JsonResponse({"message":"item added"})