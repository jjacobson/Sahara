# users/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput

from .models import CustomUser


# register form
class CustomUserCreationForm(UserCreationForm):
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

    class Meta(UserCreationForm):
        fields = ('first_name', 'last_name', 'email', "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # firstname
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"

        # lastname
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"

        # email
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "Email Address"

        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': "form-control"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': _("Password")})


class CustomUserChangeForm(UserChangeForm):

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

    class Meta(UserCreationForm):
        fields = ('first_name', 'last_name', 'email')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)

        # firstname
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"

        # lastname
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"

        # email
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "Email Address"

        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': _("Password")})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': _("Password")})
