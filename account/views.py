import random
import uuid

from django.contrib.auth import login, mixins, logout
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.backends.utils import csrf_input
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from account import mixins
from account.forms import LoginForm, RegisterForm, VerifyCode, ForgotForm, ForgotCode, NewPasswordForm
from account.models import User


# Create your views here.


class Login(mixins.RediretToHome, View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request: HttpRequest):
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(phone=mobile)
                if check_password(password, user.password):
                    if user.is_active:
                        login(request, user)
                        if user.is_superuser or user.is_staff:
                            return redirect(reverse('home'))
                        else:
                            return redirect(reverse('installments'))
                    else:
                        form.add_error('password', 'حساب کاربری شما هنوز فعال نشده است')
                else:
                    form.add_error('password', 'موبایل یا رمز عبور صحیح نیست')
                    return render(request, 'account/login.html', {'form': form})
            except User.DoesNotExist:
                form.add_error('password', 'موبایل یا رمز عبور صحیح نیست')
                return render(request, 'account/login.html', {'form': form})

        return render(request, 'account/login.html', {'form': form})


class Register(mixins.RediretToHome, View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request: HttpRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']

            user = User.objects.filter(username=username, phone=mobile)
            if user.exists():
                form.add_error('username', 'نام کاربری وارد شده از قبل وجود دارد')
                form.add_error('mobile', 'قبلا با این شماره ثبت نام شده است')
                return render(request, 'account/register.html', {'form': form})
            else:
                request.session['registration_info'] = {
                    'username': username,
                    'mobile': mobile,
                    'password': password,
                }
                request.session['random_code'] = random.randint(111111, 999999)

                print(request.session.get('random_code'))  # todo: SET send sms code for user

                verify_form = VerifyCode()
                return JsonResponse({
                    'status': 'input_code',
                    'body': render_to_string('account/register_code_js.html', {'form': verify_form, 'csrf': csrf_input(request)})
                })
        return JsonResponse({
            'status': 'errors',
            'errors': form.errors
        })


class VerifyRegistration(mixins.RediretToHome, View):
    def post(self, request):
        form = VerifyCode(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            print(request.session.get('random_code'))
            if str(code) == str(request.session.get('random_code')):
                register_info = request.session.get('registration_info')
                new_user = User(username=register_info['username'], phone=register_info['mobile'], is_active=True, is_superuser=False, is_staff=False)
                new_user.set_password(register_info['password'])
                new_user.save()
                login(request, new_user)
                return JsonResponse({
                    'status': 'success'
                })
            else:
                return JsonResponse({
                    'status': 'invalid',
                    'msg': 'کد وارد شده صحیح نمیباشد'
                })

        return JsonResponse({
            'status': 'errors',
            'errors': form.errors
        })


class ForgotPassword(mixins.RediretToHome, View):
    def get(self, request):
        form = ForgotForm()
        return render(request, 'account/forgot_password.html', {'form': form})

    def post(self, request):
        form = ForgotForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['mobile']

            try:
                user = User.objects.get(phone=phone)
                request.session['phone_number'] = user.phone
                forgot_form = ForgotCode()
                request.session['forgot_random_code'] = random.randint(111111, 999999)
                print(request.session.get('forgot_random_code'))  # todo: SET send sms code for user
                return JsonResponse({
                    'status': 'receive_code',
                    'body': render_to_string('account/forgot_code_js.html', {'form': forgot_form, 'csrf': csrf_input(request)})
                })

            except User.DoesNotExist:
                return JsonResponse({
                    'status': 'not_found',
                    'msg': 'کاربر یافت نشد!'
                })

        render(request, 'account/forgot_password.html', {'form': form})


class VerifyForgotPassword(mixins.RediretToHome, View):
    def post(self, request):
        form = ForgotCode(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if str(code) == str(request.session.get('forgot_random_code')):
                new_password = NewPasswordForm()
                return JsonResponse({
                    'status': 'success',
                    'body': render_to_string('account/set_password.html', {'form': new_password, 'csrf': csrf_input(request)})
                })
            else:
                return JsonResponse({
                    'status': 'invalid',
                    'msg': 'کد وارد شده صحیح نمیباشد'
                })

        return JsonResponse({
            'status': 'errors',
            'errors': form.errors
        })


class SetNewPassword(mixins.RediretToHome, View):
    def post(self, request):
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            user = User.objects.get(phone=request.session.get('phone_number'))
            if check_password(password, user.password):
                form.add_error('password', 'پسورد وارد شده با پسورد فعلی یکسان است')
            else:
                user.set_password(password)
                user.save()
                return JsonResponse({
                    'status': 'changed',
                    'body': render_to_string('account/password_success_change.html')
                })
        return JsonResponse({
            'status': 'errors',
            'errors': form.errors
        })


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
