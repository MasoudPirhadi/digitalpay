from django import forms
from django.core.exceptions import ValidationError

from account.models import User


class LoginForm(forms.Form):
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control inputBrClass',
        'placeholder': 'موبایل'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control inputBrClass',
        'placeholder': 'رمز ورود'
    }))


class RegisterForm(forms.Form):
    username = forms.CharField(label="نام کاربری", widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری',
        'class': 'form-control'
    }))
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'موبایل'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'رمز عبور'
    }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تکرار رمز عبور'
    }))

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError('رمز عبور و تکرار آن یکسان نیستند')

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if User.objects.filter(phone=mobile).exists():
            raise ValidationError('قبلا با این شماره ثبت نام شده است')
        return mobile

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('نام کاربری وارد شده از قبل وجود دارد')
        return username


class VerifyCode(forms.Form):
    code = forms.IntegerField(label='کد تایید', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'کد تایید'
    }))


class ForgotForm(forms.Form):
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'موبایل'
    }))


class ForgotCode(forms.Form):
    code = forms.IntegerField(label='کد تایید', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'کد تایید'
    }))


class NewPasswordForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'رمز عبور'
    }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تکرار رمز عبور'
    }))

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError('رمز عبور و تکرار آن یکسان نیستند')
