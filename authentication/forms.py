from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form extending Django's UserCreationForm.
    Includes additional fields for first_name, last_name, and email.
    """
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required. Enter your first name.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required. Enter your last name.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes to existing fields
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })

    def clean_email(self):
        """
        Validate that the email is unique.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        """
        Save the user with the additional fields.
        """
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.
    Allows editing of first_name, last_name, email, and username.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        """
        Validate that the email is unique (excluding current user).
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_username(self):
        """
        Validate that the username is unique (excluding current user).
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("A user with this username already exists.")
        return username


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Custom password change form with Bootstrap styling.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes to password fields
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Current Password'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'New Password'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        })