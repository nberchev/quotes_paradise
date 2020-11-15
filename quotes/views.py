from django.shortcuts import render
from django.views import generic

from quotes.models import Quote


class QuotesList(generic.ListView):
    model = Quote
    template_name = 'quotes/quotes_list.html'
    context_object_name = 'quotes'


class MyQuotes(generic.ListView):
    model = Quote
    template_name = 'quotes/quotes_list.html'
    context_object_name = 'quotes'
