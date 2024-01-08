from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .models import DigitalRoad


STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('ongoing', 'Ongoing')
    )

CHOICES = (
        ('publicwifi', 'Public Wifi'),
        ('lastmile', 'Last Mile'),
        ('backbone', 'Backbone')
    )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
                                
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class AddRecordForm(forms.ModelForm):
    region = forms.CharField(max_length=255, required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Region'}), label="")
    county = forms.CharField(max_length=255, required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'County'}), label="")
    sub_county = forms.CharField(max_length=255, required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub County'}), label="")
    name_of_site = forms.CharField(max_length=255, required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Site'}), label="")
    type_of_site = forms.ChoiceField(choices=CHOICES, required=True, widget=forms.widgets.ChoiceWidget(attrs={'class': 'form-control', 'placeholder': 'Type of Site'}), label="")
    status = forms.ChoiceField( choices=STATUS_CHOICES, required=True, widget=forms.widgets.ChoiceWidget(attrs={'class': 'form-control', 'placeholder': 'Status'}), label="")
    no_of_aps = forms.IntegerField( required=True, widget=forms.widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'No of Aps'}), label="")
    date_surveyed = forms.DateField( required=True, widget=forms.widgets.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Surveyed'}), label="")
    date_installed = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Installed'}), label="")
    contractor = forms.CharField(max_length=255, required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contractor'}), label="")
    boq_amount = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'BOQ Amount'}), label="")
    insspection_status = forms.DateField (required=True, widget=forms.widgets.DateInput(attrs={'class': 'form-control', 'placeholder': 'Record ID'}), label="")
    inspection_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={'class': 'form-control', 'placeholder': 'Inspection Date'}), label="")

    class Meta:
        model = DigitalRoad
        exclude = ("user",)