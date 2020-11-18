from django import forms

from quotes.models import Quote


class QuoteForm(forms.ModelForm):
    author = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', }),)
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', }),)
    image_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control', }),)

    class Meta:
        model = Quote
        fields = ('text', 'author', 'image_url')
