from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=90)
    last_name = forms.CharField(max_length=90)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=90)
