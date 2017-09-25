from django.shortcuts import redirect, render
from lists.models import Item, List


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items' : items})
<<<<<<< HEAD
<<<<<<< HEAD


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
=======
>>>>>>> parent of 36ad968... URLs for forms x2, moved code in views + tests, new URL
=======
>>>>>>> parent of 36ad968... URLs for forms x2, moved code in views + tests, new URL
