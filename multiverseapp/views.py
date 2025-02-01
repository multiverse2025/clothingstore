from django.shortcuts import render
from .models import Designs
from .models import Products

# Create your views here.

def home(request):
    return render (request,"home.html")

def designs(request):
    all_designs = Designs.objects.all()  
    return render(request, "designs.html", {"designs": all_designs})

def design_detail(request, product_id):
    design = Designs.objects.get(product_id=product_id)
    return render(request, "design_detail.html", {"design": design})

def custom(request):
    return render (request ,"custom.html")

def products(request):
    all_products = Products.objects.all()  
    return render (request,"products.html",{"products":all_products})

def about(request):
    return render(request,"about.html")