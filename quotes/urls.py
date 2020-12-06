from django.urls import path

from quotes.views import all_quotes_list, MyQuotes, CreateQuote, quote_details, DeleteQuote, EditQuote, like_quote, \
    pie_chart

urlpatterns = [
    path('', all_quotes_list, name='all quotes'),
    path('my_quotes/', MyQuotes.as_view(), name='my quotes'),
    path('create/', CreateQuote.as_view(), name='create quote'),
    path('details/<int:pk>/', quote_details, name='quote details'),
    path('delete/<int:pk>/', DeleteQuote.as_view(), name='delete quote'),
    path('edit/<int:pk>/', EditQuote.as_view(), name='edit quote'),
    path('like/<int:pk>/', like_quote, name='like quote'),
    path('pie_chart/', pie_chart, name='pie chart'),
]
