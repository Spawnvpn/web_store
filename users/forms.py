import datetime
from django.contrib.auth import authenticate, models
from django import forms
from django.forms.widgets import MultiWidget, Select, TextInput
from users.models import WebStoreUser
from django.utils.translation import ugettext as _


class PhoneWidget(MultiWidget):
    def __init__(self, attrs=None, **kwargs):
        widgets = [Select(choices=(('38', '38'), ('7', '7'), ('1', '1'),)),
                   Select(choices=(('050', '050'), ('095', '095'),
                                   ('099', '099'), ('066', '066'),
                                   ('067', '067'), ('068', '068'),
                                   ('063', '063'), ('093', '093'),)),
                   TextInput(attrs={'size': 7, 'max_length': 7})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.operator, value.number]
        return ["", "", ""]

    def format_output(self, rendered_widgets):
        return "+" + rendered_widgets[0] + "(" + rendered_widgets[1] + ")" + rendered_widgets[2]


class PhoneField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        list_fields = [forms.CharField(),
                       forms.CharField(),
                       forms.CharField()]
        super(PhoneField, self).__init__(
            list_fields, widget=PhoneWidget(), *args, **kwargs)

    def compress(self, values):
        return values[0] + values[1] + values[2]


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label=_('Username'))
    password1 = forms.CharField(widget=forms.PasswordInput, label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_('Password confirm'))
    email = forms.EmailField(label=_('Email'))
    birth_date = forms.DateField(label=_('Birth date'))
    phone_number = PhoneField(label=_('Phone number'))

    def clean_birth_date(self):
        date = self.cleaned_data.get('birth_date')
        today = datetime.date.today()
        if date.year >= today.year - 18:
            raise forms.ValidationError("You must grow up")
        return date

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    class Meta:
        model = WebStoreUser
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "phone_number",
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'fill-container'}), label=_('Username'))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'fill-container'}), label=_('Password'))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError(message='Invalid username or password',
                                        code='invalid_login')
