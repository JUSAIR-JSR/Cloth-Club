from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request):
    products=Product.objects.order_by('id')[:3]
    return render(request,'Index.html',{'products':products})

# @login_required(login_url='login')
def list_all(request):
    all_products=Product.objects.all()
    context={
        'all_products':all_products
    }
    return render(request,'list_all.html',context)

def list_one(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'list_one.html',{'product':product})

def search(request):
    return render(request,'search.html')