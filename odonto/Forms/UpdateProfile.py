from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UpdateProfile(ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff')
        labels = (
            {
                'first_name': 'Nome',
                'last_name': 'Sobrenome',
            }
        )
        help_texts = (
            {
                'is_staff': 'Siginifica que o usuário pode criar e alterar os outros usuários'
            }
        )

    def save(self, commit=True):
        user = self.instance
        user.set_password(user.password)
        user.save()
        return user