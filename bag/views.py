from django.shortcuts import render, redirect
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
            if bag[item_id]['bean_options']['roast'] == roast and bag[item_id]['bean_options']['grind'] == grind:
                bag[item_id]['bean_options'][item_id] += quantity
            else:
                bag[item_id]['bean_options'][item_id] = quantity
        else:
            bag[item_id] = {'bean_options': {"roast": roast, "grind": grind, "qty": quantity}}

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
