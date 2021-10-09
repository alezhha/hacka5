from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Messages, Product, Category
from random import randint

# Create your views here.

def main(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "main.html", {"products":products, "categories":categories})

def contact(request):
    return render(request, "contact.html")

def detail(request, pk):
    product_pk = Product.objects.get(pk=pk)
    products = Product.objects.all()
    review = randint(0, 10000000)
    return render(request, "shop-details.html", {"product_pk":product_pk, "products":products, "review":review})





def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {"form":form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})

def signout(request):
    logout(request)
    return HttpResponseRedirect("/")




products = []
def cartAdd(request, pk):
    product_pk = Product.objects.get(pk = pk)
    products.append(product_pk)
    return render(request, 'shoping-cart.html', {'products':products, 'products_sum':"Go to Cart page!"})

def cartRem(request, pk):
    product_pk = Product.objects.get(pk = pk)
    if product_pk in products:
        products.remove(product_pk)
    return render(request, 'shoping-cart.html', {'products':products, 'products_sum':"Go to Cart page!"})

def cart(request):
    products_sum = 0
    for product in products:
        products_sum = products_sum + product.price
    return render(request, "shoping-cart.html", {'products':products, 'products_sum':products_sum})

def get_by_category(request, pk):
    products = Product.objects.filter(category=pk)
    categories = Category.objects.all()

    return render(request, 'main.html', {"products":products, "categories":categories})




def sendMessage(request):
    if request.method == 'POST':
        mess = Messages()
        mess.name = request.POST.get('name')
        mess.email = request.POST.get('email')
        mess.text = request.POST.get('text')
        mess.save()
    return HttpResponseRedirect('/')