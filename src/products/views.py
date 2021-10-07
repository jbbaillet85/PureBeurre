from django.shortcuts import render
from homepage.forms import SearchForm
from products.algoSubtitution import AlgoSubtitution, Substitution
from products.models import Product

# Create your views here.
def get_results_products(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        search_product = request.POST.get("search_product")
        print(f"keyword: {search_product}")
        if form.is_valid():
            products = AlgoSubtitution(search_product)
            form_search = SearchForm()
            print(f"products: {products}")
            context = {'form_search':form_search, 'products':products.result_search}
            return render(request, "result_products.html", context)
    else:
        form =SearchForm()
        context = {'form_search': form}
        return render(request, "homepage.html", context)

def get_caracteristiques_substitution(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        substituted = Product.objects.get(id=product_id)
        substitutions = Substitution(product_id)
        form =SearchForm()
    context = {'substituted':substituted, 'substitutions': substitutions.list_products, 'form_search': form}
    return render(request, "caracteristiques_subtitution.html", context)

def get_description_product(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)
        form =SearchForm()
    context = {'product':product, 'form_search': form}
    return render(request, "description_product.html", context )