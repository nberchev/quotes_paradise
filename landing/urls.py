from django.urls import path

from .views import load_landing_page


urlpatterns = [
    path('', load_landing_page, name='landing'),
]
