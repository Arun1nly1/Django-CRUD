from django.shortcuts import render, redirect  
from product.forms import ProductForm  
from product.models import Product 
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Payment
from .serializers import PaymentSerializer, ProductSerializer

from django.views.generic import TemplateView
 
def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect("/show") 

    form = ProductForm()  
    return render(request,'index.html',{'form':form})  

def show(request):
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products})  

def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product}) 

def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})
  
def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/show")

def raw_sql(request):
    names = []
    for p in Product.objects.raw('SELECT * FROM products'):
        names.append(p.pname)
    return JsonResponse({'result':names})

def getjson(request):
    return JsonResponse({'name':'broadway'})

def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

#Generic Views
class ExampleStaticView(TemplateView):
    template_name = "generic_templates/static.html"


#API Views
class PaymentView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Payment was successfull.'})
        return JsonResponse({'message':'Payment was not successfull.'})

    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse(serializer.data, safe=False)
