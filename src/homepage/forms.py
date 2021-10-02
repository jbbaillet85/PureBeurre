from django import forms

class SearchForm(forms.Form):
    search_product = forms.CharField(label="recherche", max_length=100)