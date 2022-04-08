from cart.models import CartModel


def intro(request):
    try:
        user_id = request.user.id
    except Exception:
        user_id = None
    context_return = dict()
    
    
    ## INFO 1: Count total Items in cart without repeating
    context_return["item_count"] = 0
    if user_id:
        user = CartModel.objects.filter(user_id=user_id)
        items = user[0].cart_items["products"]
        item_count = len(items)
        context_return["item_count"] = item_count
        
    return context_return
    
            