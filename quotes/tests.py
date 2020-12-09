from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from accounts.models import ProfileUser

from quotes.forms import QuoteForm
from quotes.models import Quote


class LandingPageTests(TestCase):
    def test_landingPage_loadsProperlyAndCorrectTemplate(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing/landing_page.html')


class QuoteViewsTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getAllQuotesList_whenNoQuotes_shouldRenderCorrectTemplateWithNoQuotes(self):
        response = self.test_client.get(reverse('all quotes'))
        self.assertTemplateUsed(response, 'quotes/all_quotes_list.html')

        quotes = response.context['quotes']
        self.assertEqual(0, len(quotes))

    def test_getAllQuotesList_whenTwoQuotes_shouldRenderCorrectTemplateWithTwoQuotes(self):
        user = User(username='testtest1', password='testmest22')
        user.save()
        profile = ProfileUser(user=user, favorite_book=None, location=None, profile_picture=None)
        profile.save()

        quotes_created = (
            Quote(user=profile, text='d', author='d', image=None),
            Quote(user=profile, text='m', author='m', image=None),
        )
        [quote.save() for quote in quotes_created]

        response = self.test_client.get(reverse('all quotes'))
        self.assertTemplateUsed(response, 'quotes/all_quotes_list.html')

        quotes = response.context['quotes']
        self.assertEqual(2, len(quotes))


class QuoteFormTests(TestCase):
    def test_valid_form(self):
        user = User(username='testtest1', password='testmest22')
        user.save()
        profile = ProfileUser(user=user, favorite_book=None, location=None, profile_picture=None)
        profile.save()

        q = Quote.objects.create(user=profile, text='Foo', author='Bar', image=None)
        data = {'user': q.user, 'text': q.text, 'author': q.author, 'image': q.image}
        form = QuoteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        user = User(username='testtest1', password='testmest22')
        user.save()
        profile = ProfileUser(user=user, favorite_book=None, location=None, profile_picture=None)
        profile.save()

        q = Quote.objects.create(user=profile, text='Foo', author='', image=None)
        data = {'user': q.user, 'text': q.text, 'author': q.author, 'image': q.image}
        form = QuoteForm(data=data)
        self.assertFalse(form.is_valid())
