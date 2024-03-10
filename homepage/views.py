from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from . models import blog_card, Bestseller, Category, Order,About
from . models import OrderItems,Product,Fabric,Saree,Kurti,Bannerimg,StoryContent,PrivacyPolicy,ShippingPolicy,TermsAndCondn,CancelRefund
from user.models import UserProfile
from decimal import Decimal
from user.forms import UserShipping,PaymentForm
import json
from django.db import transaction 
from django.conf import settings

from django.views.decorators.csrf import csrf_protect
 

def basic(request):
    template = loader.get_template('homepage/basic.html')
    return render(request,'homepage/basic.html')

def searchmatch(query,prod):
    keywords_list = [keyword.strip() for keyword in prod.keywords.split(',')]
    for keyword in keywords_list:
        if query in keyword.lower() or keyword.upper():
            return True
    else:
        return False
def search(request):
    query = request.GET.get('search')
    allprod=[]
    product = Product.objects.filter(keywords__icontains=query)
    for prod in product:
        if searchmatch(query, prod):
            allprod.append(prod)

    params = {'allprod':allprod}
    template1 = loader.get_template('homepage/search.html')
    return render(request,'homepage/search.html',params)

def mains(request):
    blg = blog_card.objects.all()
    best = Bestseller.objects.all()
    cat = Category.objects.all()
    about = About.objects.all()

    para={'blgs':blg,'best':best, 'cat':cat, 'about':about}
    template = loader.get_template('homepage/mains.html')
    return render(request,'homepage/mains.html',para)

def prodsaree(request):
    best = Saree.objects.all()
    banner = Bannerimg.objects.get(imgid=1)
    para={'best':best,'banner':banner}
    template = loader.get_template('homepage/prodsaree.html')
    return render(request,'homepage/prodsaree.html',para)

def prodsuit(request):
    best = Kurti.objects.all()
    banner = Bannerimg.objects.get(imgid=5)
    para={'best':best,'banner':banner}
    template = loader.get_template('homepage/prodsuit.html')
    return render(request,'homepage/prodsuit.html',para)

def prodfabric(request):
    best = Fabric.objects.all()
    banner = Bannerimg.objects.get(imgid=6)
    para={'best':best,'banner':banner}
    template = loader.get_template('homepage/prodfabric.html')
    return render(request,'homepage/prodfabric.html',para)

@csrf_protect
@login_required
def checkout(request):
    s_form = UserShipping()
    if request.method == 'POST':
        s_form = UserShipping(request.POST)
        if s_form.is_valid():
            # Save shipping details to the order
            total=request.POST['total']

            order = Order.objects.create(
                customer=request.user.userprofile,
                contact_number=s_form.cleaned_data['contact_number'],
                address=s_form.cleaned_data['address'],
                city=s_form.cleaned_data['city'],
                state=s_form.cleaned_data['state'],
                zipcode=s_form.cleaned_data['zipcode'],
                total=total
            )

            # Save order items
            cart = json.loads(request.POST.get('cart_data', '{}'))
            total = 0 
            with transaction.atomic():
                for item, item_data in cart.items():
                    product = Product.objects.get(pk=item)
                    quantity = item_data[0]
                    size = item_data[4] if len(item_data)>1 else ''
                    OrderItems.objects.create(
                        product=product,
                        order=order,
                        quantity=quantity,
                        size_selected=size,
                    )
                    total += product.price * quantity

                order.total = total
                order.save()
            # Optional: Clear the cart after creating order items
            return redirect('payment',order_id=order.orderId)
            
    else:
        s_form = UserShipping()

    context = {'s_form': s_form}
        
    return render(request, 'homepage/checkout.html', context)


def product(request,productId):
    products = get_object_or_404(Product,productId=productId)
    kurti_sizes = None  # Initialize kurti_sizes to None

    if products.category == 'kurti'or'kurti':  # Use lower() for case-insensitive comparison
        try:
            kurti_sizes = Kurti.objects.get(product=products).available_sizes.split(',')
        except Kurti.DoesNotExist:
            pass
    context = {
        'products': products,
        'kurti_sizes': kurti_sizes,
    }
    template1 = loader.get_template('homepage/product.html')
    return render(request, 'homepage/product.html',context)

@csrf_protect
def payment(request,order_id):
    order = get_object_or_404(Order,orderId=order_id)
    #user = User.objects.get(id=request.user.id) 
    if request.method == 'POST':
        p_form = PaymentForm(request.POST, instance=order)
        if p_form.is_valid():
            payment_method = p_form.cleaned_data.get('payment_method')
            if(payment_method=='pay_online'):
                return redirect('sorry',order_id=order.orderId)
            else:
                p_form.save()
                return redirect('success',order_id=order.orderId)
    else:
        p_form = PaymentForm(instance=order)

    
    context = {'p_form': p_form,'order':order,'order_id': order.orderId}
    template1 = loader.get_template('homepage/payment.html')
    return render(request,'homepage/payment.html',context)

def successorder(request,order_id):
    order = get_object_or_404(Order,orderId=order_id)

    context = {'order': order}
    template1 = loader.get_template('homepage/success.html')
    return render(request,'homepage/success.html',context)

def sorrymsg(request,order_id):
    order = get_object_or_404(Order,orderId=order_id)

    context = {'order': order}
    template1 = loader.get_template('homepage/sorry.html')
    return render(request,'homepage/sorry.html',context)

def deleteorder(request,order_id):
    order = get_object_or_404(Order,orderId=order_id)
    orderitem = get_object_or_404(OrderItems,order=order_id)
    orderitem.delete()
    order.delete()
    return redirect('home')

def story(request):
    story = StoryContent.objects.all()
    context = {'story':story}
    template=loader.get_template('homepage/story.html')
    return render(request,'homepage/story.html',context)

def privacy(request):
    Policy = PrivacyPolicy.objects.all()
    context = {'Policy':Policy}
    template=loader.get_template('homepage/privacy.html')
    return render(request,'homepage/privacy.html',context)

def shipping(request):
    Policy = ShippingPolicy.objects.all()
    context = {'Policy':Policy}
    template=loader.get_template('homepage/shipping.html')
    return render(request,'homepage/shipping.html',context)

def terms(request):
    Policy = TermsAndCondn.objects.all()
    context = {'Policy':Policy}
    template=loader.get_template('homepage/terms.html')
    return render(request,'homepage/terms.html',context)

def cancel(request):
    Policy = CancelRefund.objects.all()
    context = {'Policy':Policy}
    template=loader.get_template('homepage/cancel.html')
    return render(request,'homepage/cancel.html',context)
#'''def navi(request):
    #template = loader.get_template('homepage/navi.html')
    #return render(request,'homepage/navi.html')

#def blog(request):
    #template1 = loader.get_template('homepage/includes/blog.html')
    #return render(request,'homepage/includes/blog.html')

#def bestseller(request):
    #template1 = loader.get_template('homepage/bestseller.html')
    #return render(request,'homepage/bestseller.html')

#def category(request):
    #template1 = loader.get_template('homepage/category.html')
    #return render(request,'homepage/category.html')

#def about(request):
    #template1 = loader.get_template('homepage/about.html')
    #return render(request,'homepage/about.html')

#'''def checkout(request):
#    if request.user.is_authenticated:
#       cart = {}  # Initialize an empty cart dictionary
#       if 'cart' in request.session:
#           cart = request.session['cart']
#       
#       # Calculate sub_total and total
#       sub_total = Decimal(0)
#       for key, value in cart.items():
#           sub_total += Decimal(value['product'].price) * value['quantity']
#       
#       total = sub_total  # Assuming no additional costs

#       context = {
#           'cart': cart,
#           'sub_total': sub_total,
#           'total': total
#       }
        
#   else:
#       context = {}

#   return render(request, 'homepage/checkout.html', context)'''

#'''def get_user_cart(order,cart):
#    order_items_data = []
#    for item_id, quantity in cart.items():
#        product = Product.objects.get(productId=item_id)
#        order_item_data ={
#            'product_name': product.name,
#            'quantity': quantity,
#            'price': product.price,
#            'total_price': product.price * quantity,
#        }

#        order_items_data.append(order_item_data)
#        # You may want to perform additional actions here if needed
#    # Optional: Clear the cart after creating order items
#    cart.clear()
#    return order_items_data'''