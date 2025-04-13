# lexichat/forms.py

from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(
        label='Your Question',
        max_length=500,
        widget=forms.TextInput(attrs={'placeholder': 'Ask something about the Constitution...'})
    )
