from django import forms
from .models import Account


class RegistrationForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your Password',
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Confirm Password',
        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Frist Name',
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Last Name',
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Your Email Address',
        'class': 'form-control'
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter Your Phone NUmber',
        'class': 'form-control'
    }))


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForms, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "password does not match"
            )

    # def __int__(self, *args, **kwargs):
    #     super(RegistrationForms, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Fist Name'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
    #     self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
    #     self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
    #
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'input-box'
    #
