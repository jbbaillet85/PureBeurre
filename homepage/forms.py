from django import forms


class SearchForm(forms.Form):
    search_product = forms.CharField(label="",
                                     max_length=100,
                                     widget=forms.TextInput
                                     (attrs={'placeholder': '🔎Chercher'}))
