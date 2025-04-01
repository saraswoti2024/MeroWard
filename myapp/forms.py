from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Enter description', 'class': 'form-control', 'rows': 4}))