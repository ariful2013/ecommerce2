from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    username = forms.CharField(label="Enter Username", min_length=4, max_length=50, help_text='Required', widget=forms.TextInput(attrs={
        'placeholder': 'User Name',
        'class': 'form-control',
        'id': 'username'
    }))

    email = forms.CharField(label="Your Email", max_length=100, help_text='Required', error_messages={'required': 'Sorry, You will need an email'}, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
        'id': 'email'
    }))

    password1 = forms.CharField(label="Enter Password", max_length=100, help_text='Required', error_messages={'required': 'Sorry, You will need Password'}, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'id': 'password1'
    }))

    password2 = forms.CharField(label="Repeat Password", max_length=100, help_text='Required', error_messages={'required': 'Sorry, You will need Re-Password'}, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'id': 'password2'
    }))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists in Database")
        return username


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email Address", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'login-username'}))

    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'login-pwd'}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    username = forms.CharField(label="Enter Username", required=True, min_length=4, max_length=50, help_text='Required', widget=forms.TextInput(attrs={
        'placeholder': 'User Name',
        'class': 'form-control',
        'id': 'username',
        'readonly': 'readonly'
    }))

    email = forms.CharField(label="Your Email", required=True, max_length=100, help_text='Required', error_messages={'required': 'Sorry, You will need an email'}, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
        'id': 'email',
        'readonly': 'readonly'
    }))

    first_name = forms.CharField(label="First name", min_length=4, max_length=50, help_text='Required', widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control',
        'id': 'first_name'
    }))

    last_name = forms.CharField(label="Last name", min_length=4, max_length=50, help_text='Required', widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control',
        'id': 'last_name'
    }))


class PwdResetForm(PasswordResetForm):
    email = forms.CharField(label="Your Email", required=True, max_length=100, help_text='Required', error_messages={'required': 'Sorry, You will need an email'}, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
        'id': 'form-email',
    }))

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email)
        if not user:
            raise forms.ValidationError(
                'Unfortunately we can not find that email address')

        return email


class PwdResetConfirmForm(SetPasswordForm):

    new_password1 = forms.CharField(label="Enter Password", max_length=100, help_text='Required', error_messages={'required': 'Sorry, You will need Password'}, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'id': 'new_password1'
    }))

    new_password2 = forms.CharField(label="Repeat Password", max_length=100, help_text='Required', error_messages={'required': 'Sorry, You will need Re-Password'}, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'id': 'new_password2'
    }))
