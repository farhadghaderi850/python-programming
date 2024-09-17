from django import forms


class MyappForm(forms.Form):
    title = forms.CharField()
    text = forms.TextInput()
    is_enable = forms.BooleanField()
    publish_date = forms.DateField()
