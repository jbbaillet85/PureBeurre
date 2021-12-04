from django.shortcuts import render
from homepage.forms import SearchForm
from products.algoSubtitution import AlgoSubtitution, Substitution
from products.algoSubtitution import ProductsOfFavorites
from django.contrib.auth.decorators import login_required
from products.models import Product, Favorites

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
            context = {'form_search': form_search,
                       'products': products.result_search,
                       "search_product": search_product}
            return render(request, "result_products.html", context)
    else:
        form = SearchForm()
        context = {'form_search': form}
        return render(request, "homepage.html", context)


def get_choice_substitution(request):
    form = SearchForm()
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        substituted = Product.objects.get(id=product_id)
        substitutions = Substitution(product_id)
    context = {'substituted': substituted,
               'substitutions': substitutions.list_products,
               'form_search': form}
    return render(request, "choice_subtitution.html", context)


@login_required(login_url='login')
def get_description_product(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)
        form = SearchForm()
    context = {'product': product, 'form_search': form}
    return render(request, "description_product.html", context)


@login_required(login_url='login')
def get_favorites(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
    try:
        print(f"product_id: {product_id}")
        print(f"user: {request.user.id}")
        Favorites.objects.create(
            product_id=product_id,
            user_id=request.user.id)
    except: # noqa
        print("Le favori est déjàs enregistré")
    user = request.user.id
    try:
        favorites = ProductsOfFavorites(user)
    except: # noqa
        favorites = None
    form = SearchForm()
    context = {'favorites': favorites.products, 'form_search': form}
    return render(request, "favorites.html", context)
