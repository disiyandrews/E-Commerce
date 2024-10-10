from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import userdetails,Category,Product,Cart


# Create your views here.

def home(request):
    return render(request,'home.html')


def loginn(request):
    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')


def adminpanel(request):
    return render(request,'adminpanel.html')



def register(request):
    if request.method == 'POST':
        fname = request.POST['std_name']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pswd = request.POST['pass']
        cpswd = request.POST['cpass']
        email = request.POST['email']
        addr = request.POST['addr']
        
        cnum = request.POST['cnum']
        img = request.FILES.get('img')

        if pswd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This username already exists!')
                return redirect('signup')
            else:
                # Create the user
                user = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    password=pswd,
                    email=email
                )
                user.save()

                # Create user details
                teacher = userdetails(
                    address=addr,
                    number=cnum,
                    usimg=img,
                    user=user
                )
                teacher.save()

                messages.success(request, 'Registration successful!')
                return redirect('loginn')
        else:
            messages.info(request, 'Passwords do not match.')

    return redirect('signup')



def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            # If the user is staff, redirect to admin panel
            if user.is_staff:
                auth.login(request, user)  # Log the user in
                return redirect('adminpanel')
            else:
                # Redirect normal users to the home page
                auth.login(request, user)
                return redirect('userpanel')
        else:
            # Invalid login credentials
            messages.info(request, 'Invalid username or password')
            return redirect('home')

    # If GET request, render the login form
    return render(request, 'home.html')




def userdetail(request):
    u = userdetails.objects.all()
    return render(request,'userdetails.html',{'users': u})


def logout(request):
    auth.logout(request)
    return redirect('home')




def add_category(request):
    return render(request,'add_category.html')


def categoryadd(request):
    if request.method=='POST':
        cat_name=request.POST['category_name']
        desc=request.POST['description']
        add=Category(category_name=cat_name,description=desc)
        add.save()
        return redirect('adminpanel')


def prdt(request):
    pdt=Category.objects.all()
    return render(request,'add_product.html',{'pr':pdt})


def product_add(request):
    if request.method=='POST':
        sname=request.POST['prname']
        add=request.POST['price']
        age=request.POST['description']
        image = request.FILES.get('img')
        
        sel=request.POST['sel']
        product1=Category.objects.get(id=sel)
        std=Product(prname=sname,prprice=add,prdesc=age,primg=image,category=product1)
        std.save()
        return redirect('product_add')
    return render(request, 'add_product.html')




def viewproduct(request):
    p = Product.objects.all()
    return render(request,'view_product.html',{'vi': p})









def userpanel(request):
    cat=Category.objects.all()
    ct = Cart.objects.all()
    return render(request,'userpanel.html',{"category":cat,"cart":ct})


# def cart(request):
#     cat=Category.objects.all()
#     return render(request,'cart.html',{"category":cat})


# def category_detail(request, pk):
#     category = Category.objects.get(pk=pk)
#     products = Product.objects.filter(category=category)
#     return render(request, 'category_detail.html', {'category': category, 'products': products})



def delete_pr(request, pk):
    student = Product.objects.get(id=pk)
    student.delete()
    return redirect('viewproduct')



def delete_us(request,pk):
    te=userdetails.objects.get(user=pk)
    us=User.objects.get(id=pk)
    te.delete()
    us.delete()
    return redirect('userdetail')





# @login_required(login_url='login_page')
# def add_cart(request,pd):
#     pdt = Product.objects.get(id=pd)
#     user_id = request.user.id
#     usr = User.objects.get(id=user_id)
#     ct = Cart(user=usr,prod=pdt)
#     ct.save()
#     return redirect('cart')







def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    ct = Cart.objects.all()
    return render(request, 'category_detail.html', {'category': category, 'products': products ,"cart":ct})


def cart(request):
    current_user = request.user
    crt = Cart.objects.filter(user=current_user)
    num = len(crt)
    cat = Category.objects.all()
    ct = Cart.objects.all()
    user_id = request.user.id
    total = sum(item.subtotal() for item in ct if item.user.id == user_id)
    return render(request,'cart.html',{'category':cat,"cart":ct,'ttl':total, 'number':num})


  


def add_cart(request,pd):
    pdt = Product.objects.get(id=pd)
    user_id = request.user.id
    usr = User.objects.get(id=user_id)
    cart_item ,created = Cart.objects.get_or_create(user=usr,prod=pdt)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')



def increment_quantity(request, pk):
    cart_item = Cart.objects.get(pk=pk)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrement_quantity(request, pk):
    cart_item = Cart.objects.get(pk=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove(requst,ct):
    crt = Cart.objects.get(id=ct)
    crt.delete()
    return redirect('cart')



def checkout(request):
    return render(request, 'checkout.html')










