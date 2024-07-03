from django.shortcuts import render


def ProductList(request):
    return render(request, 'store/product_list.html')


def AddProduct(request):
    return render(request, 'store/add_product.html')
