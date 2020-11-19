from django.shortcuts import render
from django.views import generic

from accounts.models import ProfileUser

from quotes.forms import QuoteForm
from quotes.models import Quote


def has_user_access_to_modify(current_user, current_object):
    profile_user = ProfileUser.objects.filter(user__pk=current_user.pk)[0]

    if current_object.user == profile_user or current_user.is_superuser:
        return True
    else:
        return False


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


class QuoteDetails(generic.DetailView):
    model = Quote
    template_name = 'quotes/quote_details.html'
    context_object_name = 'quote'

    def get_context_data(self, **kwargs):
        context = super(QuoteDetails, self).get_context_data(**kwargs)

        if has_user_access_to_modify(self.request.user, self.get_object()):
            context['is_user_author_or_admin'] = True
        else:
            context['is_user_author_or_admin'] = False

        return context


class DeleteQuote(generic.DeleteView):
    model = Quote
    template_name = 'quotes/delete_quote.html'
    success_url = '/quotes/'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            quote = self.get_object()
            return render(request, 'quotes/delete_quote.html', {'quote': quote})
        else:
            return render(request, 'shared/unauthorized.html')
