from django.urls import path

from quotes.views import QuotesList


urlpatterns = [
    path('', QuotesList.as_view(), name='all quotes'),
]
