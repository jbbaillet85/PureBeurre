from django.shortcuts import render
from homepage.forms import SearchForm
from products.algoSubtitution import AlgoSubtitution

# Create your views here.


def homepage(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        search_product = request.POST.get("search_product")
        print(f"keyword: {search_product}")
        if form.is_valid():
            products = AlgoSubtitution(search_product)
            print(f"products: {products}")
            context = {'search_product': search_product,
                       'products': products.result_search}
            return render(request, "result_products.html", context)
    else:
        form = SearchForm()
    return render(request, "homepage.html", {'form_search': form})


def mentions_legales(request):
    context = {'form_search': SearchForm()}
    return render(request, "mentions_legales.html", context)
