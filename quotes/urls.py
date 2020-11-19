from django.urls import path

from quotes.views import QuotesList, MyQuotes, CreateQuote, quote_details, DeleteQuote


urlpatterns = [
    path('', QuotesList.as_view(), name='all quotes'),
    path('my_quotes/', MyQuotes.as_view(), name='my quotes'),
    path('create/', CreateQuote.as_view(), name='create quote'),
    path('details/<int:pk>/', quote_details, name='quote details'),
    path('delete/<int:pk>/', DeleteQuote.as_view(), name='delete quote'),
]
