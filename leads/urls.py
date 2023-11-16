from django.urls import path
from . import views

urlpatterns = [
    path('create_buyer/', views.create_buyer, name='create_buyer'),
    path('create_seller/', views.create_seller, name='create_seller'),
    path('create_realtor/', views.create_realtor, name='create_realtor'),
    path('buyer-list/', views.buyer_list, name='buyer_list'),
    path('seller-list/', views.seller_list, name='seller_list'),
    path('realtor-list/', views.realtor_list, name='realtor_list'),
    path('create_rent/', views.create_rent, name='create_rent'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('blogs-list/', views.blog_list, name='blog_list'),
    path('rent-list/', views.rent_list, name='rent_list'),  # URL for listing Rent instances
    path('list-page/', views.list_page, name='list_page'),
    path('success/', views.success_page, name='success_page'),

    # Apis for each model
    path('buyers/', views.BuyerListCreateAPIView.as_view(), name='buyer-list-create'),
    path('buyers/<int:pk>/', views.BuyerDetailAPIView.as_view(), name='buyer-detail'),
    path('sellers/', views.SellerListCreateAPIView.as_view(), name='seller-list-create'),
    path('sellers/<int:pk>/', views.SellerDetailAPIView.as_view(), name='seller-detail'),
    path('realtors/', views.RealtorListCreateAPIView.as_view(), name='realtor-list-create'),
    path('realtors/<int:pk>/', views.RealtorDetailAPIView.as_view(), name='realtor-detail'),
    path('rents/', views.RentListCreateAPIView.as_view(), name='rent-list-create'),
    path('rents/<int:pk>/', views.RentDetailAPIView.as_view(), name='rent-detail'),
    path('blogs/', views.BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', views.BlogDetailAPIView.as_view(), name='blog-detail'),
]
