from django.shortcuts import render

# Create your views here.
def get_products():
    return render("products.html")

