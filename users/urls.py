from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signin/', views.sign_in, name='sign_in'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]