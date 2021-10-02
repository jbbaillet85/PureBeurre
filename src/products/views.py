from django.shortcuts import render
from homepage.forms import SearchForm
from products.algoSubtitution import AlgoSubtitution

# Create your views here.
def get_results_products(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        search_product = request.POST.get("search_product")
        print(f"keyword: {search_product}")
        if form.is_valid():
            products = AlgoSubtitution(search_product)
            print(f"products: {products}")
            context = {'search_product':search_product, 'products':products.result_search}
            return render(request, "result_products.html", context)
    else:
        form =SearchForm()
        context = {'form_search': form}
        return render(request, "homepage.html", context)

def get_caracteristiques_substitution(request):
    context = {}
    return render(request, "caracteristiques_subtitution.html", context)

