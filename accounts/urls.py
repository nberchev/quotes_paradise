from django.urls import path, include

from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.profile_details, name='user profile'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
