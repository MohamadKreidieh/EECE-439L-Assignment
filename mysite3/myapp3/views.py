from django.shortcuts import render
from .forms import CreateBookForm
from .models import Book
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Book.objects.create(
                title=form_data['title'],
                author=form_data['author']
            )
            return HttpResponseRedirect('/success')
    else:
        form = CreateBookForm()

    return render(request, 'myapp3/createbook.html', {'form': form})

def success(request):
    return render(request, 'myapp3/success.html')