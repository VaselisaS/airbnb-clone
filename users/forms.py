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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password confirm does not match")
        return password

    def save(self, *args, **kwargs):
        username = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = super().save(commit=False)
        user.username = username
        user.set_password(password)
        user.save()
