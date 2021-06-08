from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.error_messages = {
            "account_inactive": _("Ваш аккаунт недействительный."),
            "email_password_mismatch": _(
                "Ваш e-mail и/или пароль указаны неверно."
            ),
            "username_password_mismatch": _(
                "Ваш логин и/или пароль указаны неверно."
            ),
        }
        login_widget = forms.TextInput(
            attrs={
                "placeholder": _("Логин"),
                "autocomplete": "username",
                "class": "form-control",
                "id": "login"
            }
        )
        login_field = forms.CharField(
            label=_("Логин"),
            widget=login_widget,
        )
        password_widget = forms.PasswordInput(
            attrs={
                "placeholder": _("Пароль"),
                "autocomplete": "current-password",
                "class": "form-control",
                "id": "password"
            }
        )
        password_field = forms.CharField(
            label=_("Пароль"),
            widget=password_widget,
        )
        remember_widget = forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "id": "remember"
            }
        )
        remember = forms.BooleanField(
            label=_("Запомнить меня"),
            required=False,
            widget=remember_widget
        )
        self.fields["login"] = login_field
        self.fields["password"] = password_field
        self.fields['remember'] = remember


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        email_field = forms.EmailField(
            label=_('E-mail'),
            widget=forms.TextInput(
                attrs={
                    "type": "email",
                    "placeholder": _("E-mail"),
                    "autocomplete": "email",
                    "class": "form-control",
                    "id": "email",
                }
            ),
        )

        username_field = forms.CharField(
            label=_("Логин"),
            widget=forms.TextInput(
                attrs={
                    "placeholder": _("Логин"),
                    "autocomplete": "username",
                    "class": "form-control",
                    "id": "username"
                }
            ),
        )
        password_field1 = forms.CharField(
            label=_("Пароль"),
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": _("Пароль"),
                    "autocomplete": "current-password",
                    "class": "form-control",
                    "id": "password1"
                }
            ),
        )
        password_field2 = forms.CharField(
            label=_("Повторите пароль"),
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": _("Пароль"),
                    "autocomplete": "current-password",
                    "class": "form-control",
                    "id": "password2"
                }
            ),
        )
        self.fields["email"] = email_field
        self.fields["username"] = username_field
        self.fields["password1"] = password_field1
        self.fields["password2"] = password_field2

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
