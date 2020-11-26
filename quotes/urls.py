from django.urls import path

from quotes.views import QuotesList, MyQuotes, CreateQuote, QuoteDetails, DeleteQuote, EditQuote, like_quote


urlpatterns = [
    path('', QuotesList.as_view(), name='all quotes'),
    path('my_quotes/', MyQuotes.as_view(), name='my quotes'),
    path('create/', CreateQuote.as_view(), name='create quote'),
    path('details/<int:pk>/', QuoteDetails.as_view(), name='quote details'),
    path('delete/<int:pk>/', DeleteQuote.as_view(), name='delete quote'),
    path('edit/<int:pk>/', EditQuote.as_view(), name='edit quote'),
    path('like/<int:pk>/', like_quote, name='like quote'),
]
