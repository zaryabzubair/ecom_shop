from django.shortcuts import render
from ecom_shop.settings import FIREBASE_CONFIG
import pyrebase

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()
storage = firebase.storage()


def ProductList(request):
    products = db.child('products').get().key()
    return render(request, 'store/product_list.html', {'products': products})


def AddProduct(request):
    return render(request, 'store/add_product.html')
