from django import forms


class WordCountForm(forms.Form):
    url = forms.URLField(
        required=True,
        label='URL',
        widget=forms.URLInput(attrs={
            'placeholder': 'Enter URL',
        })
    )
    word = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter word',
        })
    )
