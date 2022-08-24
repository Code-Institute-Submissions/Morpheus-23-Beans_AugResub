from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ a view to return the bag contents"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add quantity of a specific item to the bag"""

    product = get_object_or_404(Product, pk=item_id)
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
            counter = 0
            for bean_item in bag[item_id]['bean_items']:
                if bean_item['roast'] == roast and bean_item['grind'] == grind:
                    bean_item['qty'] += quantity
                    is_new_item = False
                    break
                counter +=1
            if is_new_item:
                # from https://stackoverflow.com/questions/39375250/in-python-append-dictionary-value-with-each-element-in-array
                new_bean_item = [{"roast": roast, "grind": grind, "qty": quantity}]
                bag[item_id]['bean_items'].extend(new_bean_item)
                messages.success(request,
                    (f'Added {quantity} {roast.upper()} roasted {grind.upper()} ground '
                    f'{product.name} to your bag.'))
            else:
                messages.success(request,
                    (f'Updated {roast.upper()} roasted {grind.upper()} ground '
                    f'{product.name} quantity to '
                    f'{bag[item_id]["bean_items"][counter]["qty"]}'))

        else:
            bag[item_id] = {'bean_items': [{"roast": roast, "grind": grind, "qty": quantity}]}
            messages.success(request,
                (f'Added {quantity} {roast.upper()} roasted {grind.upper()} ground '
                f'{product.name} to your bag.'))
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, (f'Updated {product.name} ' f'quantity to {bag[item_id]}'))
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {quantity} {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    roast = None
    grind = None
    if 'product_roast' in request.POST:
        roast = request.POST['product_roast']
    if 'product_grind' in request.POST:
        grind = request.POST['product_grind']

    bag = request.session.get('bag', {})

    if roast or grind:
        counter = 0
        #loop through the items and find the matching bean_item
        for bean_item in bag[item_id]['bean_items']:
            if bean_item['roast'] == roast and bean_item['grind'] == grind:
                if quantity > 0:
                    bean_item['qty'] = quantity
                    messages.success(request,
                        (f'Updated {roast.upper()} roasted {grind.upper()} ground '
                        f'{product.name} quantity to {quantity}'))
                else:
                    # if qty is zero remove the bean item from the bag
                    del bag[item_id]['bean_items'][counter]
                    # if the bean items are empty the item is also removed
                    if len(bag[item_id]['bean_items']) == 0:
                        bag.pop(item_id)
                    messages.success(request,
                        (f'Removed {roast.upper()} roasted {grind.upper()} ground '
                        f'{product.name} from your bag'))
                # get out
                break
            # move to the next item
            counter =+ 1
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, (f'Updated {product.name} ' f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request, (f'Updated {product.name} from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        roast = None
        grind = None
        if 'roast' in request.POST:
            roast = request.POST['roast']
        if 'grind' in request.POST:
            grind = request.POST['grind']

        bag = request.session.get('bag', {})

        if roast or grind:
            counter = 0
            #loop through the items and find the matching bean_item
            for bean_item in bag[item_id]['bean_items']:
                if bean_item['roast'] == roast and bean_item['grind'] == grind:
                    # remove the bean item from the bag
                    del bag[item_id]['bean_items'][counter]
                    # if the bean items are empty the item is also removed
                    if len(bag[item_id]['bean_items']) == 0:
                        bag.pop(item_id)
                    messages.success(request,
                        (f'Removed {roast.upper()} roasted {grind.upper()} ground '
                        f'{product.name} from your bag'))
                    # and exit
                    break
                counter += 1
        else:
            bag.pop(item_id)
            messages.success(request, (f'Removed {product.name} from your bag'))

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as exception:
        messages.error(request, f'Error removing item: {exception}')
        return HttpResponse(status=500,)