from django import forms
from .models import Appointments
class appoinment_form(forms.ModelForm):
    class Meta:
        model=Appointments
        fields=('name','age','gender','phone','doctor','date')
        widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'})
        }