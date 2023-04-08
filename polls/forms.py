from django import forms

class StdForm(forms.Form):
    studentID = forms.IntegerField()
    name = forms.CharField(max_length=30)
    query = forms.CharField(max_length=1000)