from cart.models import CartModel


def default_cart(request,user_id):
    cart_items = dict()
    cart_items['products'] = [[0,0,0]]
    
    obj = CartModel.objects.create(user_id=user_id,cart_items=cart_items)
    return obj
