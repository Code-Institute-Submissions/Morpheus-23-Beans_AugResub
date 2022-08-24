from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
import json

# Create your views here.


def view_bag(request):
    """ a view to return the bag contents"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add quantity of a specific item to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    roast = None
    grind = None
    if 'product_roast' in request.POST:
        roast = request.POST['product_roast']
    if 'product_grind' in request.POST:
        grind = request.POST['product_grind']

    bag = request.session.get('bag', {})

    if roast or grind:
        if item_id in list(bag.keys()):
            is_new_item = True
            for bean_item in bag[item_id]['bean_items']:
                if bean_item['roast'] == roast and bean_item['grind'] == grind:
                    bean_item['qty'] += quantity
                    is_new_item = False
                    break
            if is_new_item:
                # from https://stackoverflow.com/questions/39375250/in-python-append-dictionary-value-with-each-element-in-array
                new_bean_item = [{"roast": roast, "grind": grind, "qty": quantity}]
                bag[item_id]['bean_items'].extend(new_bean_item)
        else:
            bag[item_id] = {'bean_items': [{"roast": roast, "grind": grind, "qty": quantity}]}

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
