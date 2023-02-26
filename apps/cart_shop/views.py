from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.cart_shop.models import Product, WishItemShop, Cart, CartItemShop
from decimal import Decimal
# class ViewCart(View):
#     def get(self, request):
#         return render(request, 'cart_shop/cart.html')
class ViewCart(View):
    def get(self, request, product_id):
        if request.user.is_authenticated:
            save_product_in_cart(request, product_id)
            return redirect('cart_shop:cart')
        return redirect('auth_shop:login')

class ViewCartBuy(View):
   def get(self, request):
       if request.user.is_authenticated:
           cart_items = CartItemShop.objects.filter(cart__user=request.user)
           data = list(cart_items)
           total_price_no_discount = int(sum(item.product.price * item.quantity
                                         for item in data))
           total_discount = sum(item.product.price * item.product.discount * item.quantity
                                for item in data if item.product.discount is not None)/100
           total_sum = total_price_no_discount - total_discount
           context = {'cart_items': data,
                      'total_price_no_discount': total_price_no_discount,
                      'total_discount': total_discount,
                      'total_sum': total_sum,
                      }
           return render(request, 'cart_shop/cart.html', context)
       return redirect('auth_shop:login')


class ViewsCartAdd(View):
    def get(self, request, product_id):
        if request.user.is_authenticated:
            save_product_in_cart(request, product_id)
            return redirect('home:index')
        return redirect('auth_shop:login')

def save_product_in_cart(request, product_id):
    cart_items = CartItemShop.objects.filter(cart__user=request.user, product__id=product_id)
    if cart_items:
        cart_item = cart_items[0]
        cart_item.quantity +=1
    else:
        product = get_object_or_404(Product, id=product_id)
        cart_user = get_object_or_404(Cart, user=request.user)
        cart_item = CartItemShop(cart=cart_user, product=product)
    cart_item.save()
    return redirect('cart_shop:cart')


#class ViewWish(View):
    #def get(self, request):
        #return render(request, 'cart_shop/wishlist.html')
#
# class ViewCartDel(View):
#     def get(self, request, item_id):
#         cart = fill_card_in_session(request)
#         cart_id = fill_id_card_in_session(request)
#         if request.user.is_authenticated:
#             cart_item = get_object_or_404(CartItemShop, cart__id=cart_id, product__id=item_id)
#             cart_item.delete()
#         cart.pop(str(item_id))
#         request.session["cart"] = cart
#         return redirect('cart_shop:cart')
class ViewCartDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemShop, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:cart')

def save_in_wishlist(request, product_id):
    wishlist_items = WishItemShop.objects.filter(wishlist__user=request.user, product__id=product_id)
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Cart, user=request.user)
    wishlist_item = WishItemShop(wishlist=wishlist, product=product)
    wishlist_item.save()

class ViewWishList(View):
    def get(self, request):
        if request.user.is_authenticated:
            wishlist_items = WishItemShop.objects.filter(wishlist__user=request.user)
            data = list(wishlist_items)
            context = {'wishlist_items': data}

            return render(request, 'cart_shop/wishlist.html', context)
        return redirect('auth_shop:login')


class WishListAdd(View):
    #def get(self, request, product_id):
        #if request.user.is_authenticated:
            #save_in_wishlist(request, product_id)
            #return redirect('cart_shop:wishlist')

        #return redirect('auth_shop:login')
    #пробный вариант
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        wish_user = get_object_or_404(Cart, user=request.user)
        wish_item= WishItemShop(cart=wish_user, product=product)
        wish_item.save()
        return redirect('cart_shop:wishlist')
        # if request.user.is_authenticated:
        #     wishlist_items = WishItemShop.objects.filter(wishlist__user=request.user,
        #                                                  product__id=product_id)
        #     if wishlist_items:
        #         wishlist_item = wishlist_items[0]
        #
        #     else:
        #         product = get_object_or_404(Product, id=product_id)
        #         wish_user = get_object_or_404(Cart, user=request.user)
        #         wishlist_item = WishItemShop(cart=wish_user, product=product)
        #         wishlist_item.save()
        #     return redirect('cart_shop:wishlist')
        #
        # return redirect('auth_shop:login')

class DelWishlist(View):
    def get(self, request, item_id):
        wishlist_item = get_object_or_404(WishItemShop, id=item_id)
        wishlist_item.delete()
        return redirect('cart_shop:wishlist')

