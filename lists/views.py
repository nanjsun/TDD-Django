from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
<<<<<<< HEAD
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world')

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})

def view_list(request):
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})
=======
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
>>>>>>> chapter6
