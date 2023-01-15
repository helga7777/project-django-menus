from django.shortcuts import render
from .models import Project, Generalmenu, GeneralmenuItem, Subcategory

def menus_index(request):
    menus = Generalmenu.objects.all()
    menus_items = GeneralmenuItem.objects.all()
    cat_menu = [f'{p.order}:{p.subcat}' for p in menus_items]
    context = {
        'menus': menus,
        'menus_items': menus_items,
        'cat_menu': cat_menu,
    }
    return render(request, 'menus_index.html', context)

def menus_detail(request, pk):
    subcat = Subcategory.objects.all()
    id_subcat = Subcategory.objects.get(id_subcat=pk)
    menus = Generalmenu.objects.all()
    menus_items = GeneralmenuItem.objects.all()
    cat_menu = [f'{p.order}:{p.subcat}' for p in menus_items]
    context = {
        'id_subcat': id_subcat,
        'menus': menus,
        'menus_items': menus_items,
        'cat_menu': cat_menu,
        'subcat': subcat,
    }
    return render(request, 'menus_detail.html', context)


