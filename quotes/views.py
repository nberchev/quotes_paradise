from django.shortcuts import render
from django.views import generic

from accounts.models import ProfileUser

from quotes.forms import QuoteForm
from quotes.models import Quote


class QuotesList(generic.ListView):
    model = Quote
    template_name = 'quotes/quotes_list.html'
    context_object_name = 'quotes'


class MyQuotes(generic.ListView):
    model = Quote
    template_name = 'quotes/quotes_list.html'
    context_object_name = 'quotes'

    def get_queryset(self):
        user_profile = ProfileUser.objects.filter(user__pk=self.request.user.id)[0]
        quotes = Quote.objects.filter(user=user_profile)

        if quotes:
            return quotes
        return []


class CreateQuote(generic.CreateView):
    form_class = QuoteForm
    template_name = 'quotes/create_quote.html'
    success_url = '/quotes/'

    def form_valid(self, form):
        user_profile = ProfileUser.objects.filter(user__pk=self.request.user.id)[0]
        form.instance.user = user_profile
        return super().form_valid(form)
