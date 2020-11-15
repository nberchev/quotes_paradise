from django.urls import path, include

from . import views


urlpatterns = [
    path('profile/', views.redirect_user, name='profile'),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='user-profile'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
]
