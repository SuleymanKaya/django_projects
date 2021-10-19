from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel

class KayitForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )