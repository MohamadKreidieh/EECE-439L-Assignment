from django import forms

class CreateBookForm(forms.Form):
    title = forms.CharField(label='Title')
    author = forms.CharField(label='Author')
