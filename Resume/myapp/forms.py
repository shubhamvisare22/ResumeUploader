from django import forms
from .models import Resume
CITY_CHOICES = [
('Aurangabad','Aurangabad'),
('Beed','Beed'),
('Pune','Pune'),
('mumbai','Aurangabad')
]
GENDER_CHOICES = [
('Male', 'Male'),
('Female', 'Female'),
('Other', 'Other')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label = 'Prefered Location',choices=CITY_CHOICES, widget=forms.CheckboxSelectMultiple)
 
    class Meta:
        
        model = Resume
        fields = ("__all__")
        labels = {'name':'Full Name','dob':'Date of Birth', 'profile_pic':'Profile Photo', 'my_file':'Document',
        'pincode':'Pin Code','mobile':'Mobile Number', 'job_city':'Prefered location'}
        widgets = {
        'name':forms.TextInput(attrs={'class': 'form-control'}),
        'dob':forms.DateInput(attrs={'class': 'form-control', 'id':'datepicker'}),
        'locality':forms.TextInput(attrs={'class': 'form-control'}),
        'city':forms.TextInput(attrs={'class': 'form-control'}),
        'pincode':forms.NumberInput(attrs={'class': 'form-control'}),
        'state':forms.Select(attrs={'class': 'form-select'}),
        'mobile':forms.NumberInput(attrs={'class': 'form-control'}),
        'email':forms.EmailInput(attrs={'class': 'form-control'})
        }
