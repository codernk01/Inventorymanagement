from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Inventory,Factory
from .forms import ProductForm
from .serializer import ProductSerializer,FactorySerializer
# Create your views here.



def index (request):
    
    return render(request, 'products/index.html',{
        'products' : Inventory.objects.all()
    })

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products=Inventory.objects.all()
        serializer = ProductSerializer(products,many=True)
        return JsonResponse({'products': serializer.data}, safe=False)

    if request.method == 'POST':
        
        serializer = ProductSerializer(data= request.data)
        print ("*******",request.data, serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def product_factory_list(request,id):
    if request.method == 'GET':
        products=Inventory.objects.filter(factory=id)
        serializer = ProductSerializer(products,many=True)
        return JsonResponse({'products': serializer.data}, safe=False)
    

@api_view(['GET','POST','DELETE'])

def factory_list(request):
    if request.method == 'GET':
        factorys=Factory.objects.all()
        serializer = FactorySerializer(factorys,many=True)
      #  print(serializer.data)
        return Response({'factorys': serializer.data})

    if request.method == 'POST':
       
        serializer = FactorySerializer(data= request.data)
        #print ("*******",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

def view_product(request,id):
    product= Inventory.objects.get(pk =id)
    return HttpResponseRedirect(product,reverse('index'))

def one_product(request,id):
    product= Inventory.objects.get(pk =id)
    serializer = ProductSerializer(product)
    return JsonResponse({'product': serializer.data}, safe=False)

def add(request):
  if request.method == 'POST':
    form = ProducttForm(request.POST)
    if form.is_valid():
      new_product_number = form.cleaned_data['product_number']
      new_product_name = form.cleaned_data['product_name']
      new_product_quantity = form.cleaned_data['product_quantity']
      new_product_price = form.cleaned_data['product_price']

      new_product = Inventory(
        product_number = new_product_number,
        product_name = new_product_name,
        product_quantity = new_product_quantity,
        product_price = new_product_price
      )
      new_product.save()
      return render(request, 'products/add.html', {
        'form': ProducttForm(),
        'success': True
      })
  else:
    form = ProductForm()
  return render(request, 'products/add.html', {
    'form': ProductForm()
  })

@api_view(['GET','PUT','DELETE'])
def edit_product(request,id):
    try:
        product = Inventory.objects.get(pk=id)
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer= ProductSerializer(product,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def edit_factory(request,id):
    try:
        factory = Factory.objects.get(pk=id)
    except Factory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer= FactorySerializer(factory)
        return Response({'factory': serializer.data})
    if request.method == 'PUT':
        serializer= FactorySerializer(factory,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        factory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
