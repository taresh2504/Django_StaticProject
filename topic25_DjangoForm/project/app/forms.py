from django import forms
from .models import StudentForm

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentForm
        fields = '__all__'
    # Name = forms.CharField(max_length=50)
    # Email = forms.EmailField()
    # Contact = forms.IntegerField()
    # Age = forms.IntegerField()