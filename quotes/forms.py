from django import forms

from quotes.models import Quote


class QuoteForm(forms.ModelForm):
    # author = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', }),)
    # text = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', }),)
    # image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', }),)

    class Meta:
        model = Quote
        fields = ('text', 'author', 'image')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control',}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class SearchForm(forms.Form):
    text = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search for a Quote', }),)
