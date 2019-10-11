from django.forms import ModelForm
from django import forms
from .models import Questions
#import emoji
class Form(ModelForm):
    class Meta:
        model = Questions
        exclude = []
        widgets = {
            'question' : forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Question'}),
            'optionA' : forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Option A'}),
            'optionB' : forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Option B'}),
            'optionC' : forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Option C'}),
            'optionD' : forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Option D'}),
            'answer' : forms.NumberInput(attrs={'class':'form-control form-control-user','placeholder':'Answer'}),
            'marks' : forms.NumberInput(attrs={'class':'form-control form-control-user','placeholder':'Marks'})
        }
