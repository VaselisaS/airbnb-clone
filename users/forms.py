from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                self.cleaned_data["username"] = user.username
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong")
                )
        except models.User.DoesNotExist:
            self.add_error(
                "email", forms.ValidationError("User does not exist")
            )
