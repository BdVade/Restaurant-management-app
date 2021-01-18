from django.shortcuts import render, redirect
from .forms import OrderForm,UserUpdateForm,OrderFulfillForm
from .models import Order
from userss.models import User


# Create your views here.


def order_create_view(request, ):
    # if request.method == "POST":
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         new_order = form.save(commit=False)
    #         new_order.taker = request.user
    #         new_order.save()
    #         return render(request, 'order/create.html', {'form': form})
    # else:
    #     form = OrderForm()
    return render(request, 'order/create.html',)


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'home.html', {'orders': orders})


def manager_view(request):
    users = User.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        form = UserUpdateForm(request.POST or None,instance=User.objects.get(username=username))
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm()
    return render(request, 'order/manager.html', {'users': users,'form':form})

def kitchen_page(request):
    orders = Order.objects.all()
    if request.method == "POST":
        order_number = request.POST['order']
        form = OrderFulfillForm(request.POST or None, instance=Order.objects.get(unique_number=order_number))
        if form.is_valid():
            order = form.save(commit=False)
            order.fulfilled_by = request.user
    else:
        form = OrderFulfillForm()
    return render(request,'order/kitchen.html', {'orders':orders,'form':form})
