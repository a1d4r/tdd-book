from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item, ItemList


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    item_list = ItemList.objects.get(id=list_id)
    return render(request, 'list.html', {'list': item_list})


def new_list(request):
    item_list = ItemList.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=item_list)
    return redirect(f'/lists/{item_list.id}/')


def add_item(request, list_id):
    item_list = ItemList.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=item_list)
    return redirect(f'/lists/{item_list.id}/')
