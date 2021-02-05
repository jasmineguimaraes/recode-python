from django import forms

class CalculoFrom(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()
    operacao = forms.IntegerField()