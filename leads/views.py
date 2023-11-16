from django.shortcuts import render, redirect
from .models import Buyer, Seller, Realtor, Rent, Blog
from .forms import BuyerForm, SellerForm, RealtorForm, RentForm, BlogForm
from .serializers import BuyerSerializer, SellerSerializer, RealtorSerializer, RentSerializer, BlogSerializer
from rest_framework import generics
def create_buyer(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = BuyerForm()
    return render(request, 'buyer_form.html', {'form': form})

def create_seller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/user/dashboard/')
    else:
        form = SellerForm()
    return render(request, 'seller_form.html', {'form': form})

def create_realtor(request):
    if request.method == 'POST':
        form = RealtorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = RealtorForm()
    return render(request, 'realtor_form.html', {'form': form})

def create_rent(request):
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = RentForm()
    return render(request, 'rent_form.html', {'form': form})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})

def buyer_list(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyer_list.html', {'buyers': buyers})

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})

def rent_list(request):
    rents = Rent.objects.all()
    return render(request, 'rent_list.html', {'rents': rents})

def realtor_list(request):
    realtors = Realtor.objects.all()
    return render(request, 'realtor_list.html', {'realtors': realtors})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def list_page(request):
    buyers = Buyer.objects.all()
    sellers = Seller.objects.all()
    realtors = Realtor.objects.all()
    return render(request, 'list_page.html', {'buyers': buyers, 'sellers': sellers, 'realtors': realtors})

def success_page(request):
    return render(request, 'success_page.html')

# Apis for each model


class BuyerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class BuyerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class SellerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SellerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class RealtorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

class RealtorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

class RentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

class RentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save()  # This method handles the creation of a new Blog instance

    def perform_update(self, serializer):
        serializer.save()  # This method handles the updating of an existing Blog instance

    def perform_destroy(self, instance):
        instance.delete()  # This method handles the deletion of an existing Blog instance