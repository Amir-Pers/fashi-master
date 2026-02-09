from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username or Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(Q(username=username) | Q(email=username))
            except User.DoesNotExist:
                raise forms.ValidationError('Please enter a correct username and password. Note that both fields may be case-sensitive.')

            if not user.check_password(password):
                raise forms.ValidationError('Please enter a correct username and password. Note that both fields may be case-sensitive.')

            self.user_cache = user

        return self.cleaned_data
