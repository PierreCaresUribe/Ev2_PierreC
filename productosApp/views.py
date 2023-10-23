from django.shortcuts import render

# Create your views here.
def index(request):
    data= {}
    return render(request, 'productosApp/index.html',data)

def bebida(request):
    data= {"producto" : "Lata Pepsi",
           "producto2": "Botella Pepsi",
           "producto3" : "Nose xd",
           "url": "www.inacap.cl",
           "iamgen": "'img/stock.png'"}
    return render(request, 'productosApp/productos.html',data)

def electronica(request):
    data= {"producto" : "Mac",
           "producto2": "Lenovo",
           "producto3" : "Celular",
           "url": "www.inacap.cl",
           "iamgen": "'img/stock.png'"}
    return render(request, 'productosApp/productos.html',data)

def ropa(request):
    data= {"producto" : "GAP",
           "producto2": "NIKE",
           "producto3" : "H&M",
           "url": "www.inacap.cl",
           "iamgen": "'img/stock.png'"}
    return render(request, 'productosApp/productos.html',data)