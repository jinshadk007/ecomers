from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from store.models import Product

@login_required
def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)
