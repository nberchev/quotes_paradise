from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.db.models import Q, Count

from accounts.models import ProfileUser

from quotes.forms import QuoteForm, SearchForm
from quotes.models import Quote, Like


def has_user_access_to_modify(current_user, current_object):
    profile_user = ProfileUser.objects.filter(user__pk=current_user.pk)[0]

    if current_object.user == profile_user or current_user.is_superuser:
        return True
    else:
        return False


def extract_search_values(params):
    text = params['text'] if 'text' in params else ''

    return {'text': text, }


def all_quotes_list(request):
    params = extract_search_values(request.GET)
    quotes = Quote.objects.filter(
        Q(text__icontains=params['text']) | Q(author__icontains=params['text'])
    )

    context = {
        'quotes': quotes.annotate(num_points=Count('like')).order_by('-num_points'),
        'search_form': SearchForm(initial=params),
        }

    return render(request, 'quotes/all_quotes_list.html', context)


# class QuotesList(generic.ListView):
#     model = Quote
#     template_name = 'quotes/all_quotes_list.html'
#     context_object_name = 'quotes'


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

    def form_valid(self, form):
        user_profile = ProfileUser.objects.filter(user__pk=self.request.user.id)[0]
        form.instance.user = user_profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quote details', kwargs={'pk': self.object.pk})


# class QuoteDetails(generic.DetailView):
#     model = Quote
#     template_name = 'quotes/quote_details.html'
#     context_object_name = 'quote'
#
#     def get_context_data(self, **kwargs):
#         context = super(QuoteDetails, self).get_context_data(**kwargs)
#
#         if self.get_object().like_set.filter(user_id=self.request.user.profileuser.id).exists():
#             context['is_liked'] = True
#         else:
#             context['is_liked'] = False
#
#         try:
#             user_profile = ProfileUser.objects.filter(user__pk=self.request.user.id)[0]
#             if self.get_object().user_id == user_profile.id or self.request.user.is_superuser:
#                 context['is_user_author_or_admin'] = True
#             else:
#                 context['is_user_author_or_admin'] = False
#         except IndexError:
#             context['is_user_author_or_admin'] = False
#
#         return context


@login_required
def quote_details(request, pk):
    quote = Quote.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'quote': quote,
            'is_user_author_or_admin': quote.user_id == request.user.profileuser.id or request.user.is_superuser,
            'is_liked': quote.like_set.filter(user_id=request.user.profileuser.id).exists(),
        }

        return render(request, 'quotes/quote_details.html', context)
    else:
        context = {
            'quote': quote,
        }

        return render(request, 'quotes/quote_details.html', context)


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


class EditQuote(generic.UpdateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'quotes/edit_quote.html'

    def form_valid(self, form):
        user_profile = ProfileUser.objects.filter(user_id=self.request.user.id)[0]
        form.instance.user = user_profile
        return super().form_valid(form)

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            quote = self.get_object()
            form = QuoteForm(instance=quote)
            return render(request, 'quotes/edit_quote.html', {'quote': quote, 'form': form})
        else:
            return render(request, 'shared/unauthorized.html')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('quote details', kwargs={'pk': pk})


def like_quote(request, pk):
    like = Like.objects.filter(user_id=request.user.profileuser.id, quote_id=pk).first()

    if like:
        like.delete()
    else:
        quote = Quote.objects.get(pk=pk)
        like = Like(test=str('lk'), user=request.user.profileuser)
        like.quote = quote
        like.save()

    return redirect('quote details', pk)


def pie_chart(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            labels = []
            data = []

            queryset = Quote.objects.annotate(num_points=Count('like')).order_by('-num_points')[:5]

            for quote in queryset:
                labels.append(quote.author)
                data.append(quote.num_points)

            return render(request, 'quotes/pie_chart.html', {
                'labels': labels,
                'data': data,
            })
        else:
            return render(request, 'shared/unauthorized.html')
