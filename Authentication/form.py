

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Example: Add an email field

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) # Include the new field

class CustomLoginForm(AuthenticationForm):
    # You can add custom fields or modify the existing ones if needed
    pass