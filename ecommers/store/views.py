from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from home.models import Category
from .models import Product, search_else
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        product_count = page_products.count
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': page_products,
        'product_count': product_count
    }
    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists() # this is while the product is add inthe cart the perticular product single page add cart button will be desable

    except Exception as e:
        raise e
    context = {
        'get': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'product_detail.html', context)


def search(request):
    prod = None
    query = None
    elsecase = search_else.objects.all()
    if 'qry' in request.GET:
        query = request.GET.get('qry')
        prod = Product.objects.all().filter(Q(name__icontains=query), is_available=True)
        elsecase = None
        if len(prod) == 0:
            elsecase = search_else.objects.all()
    return render(request, 'search.html', {'qur': query, 'prod': prod, 'msg': elsecase})
