from django.urls import path

from quotes.views import QuotesList, MyQuotes, CreateQuote


urlpatterns = [
    path('', QuotesList.as_view(), name='all quotes'),
    path('my_quotes/', MyQuotes.as_view(), name='my quotes'),
    path('create/', CreateQuote.as_view(), name='create quote'),
]
