from django import forms

from account.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'email', 'avatar']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'disabled': 'disabled'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone'].disabled = True
        self.fields['username'].disabled = True


