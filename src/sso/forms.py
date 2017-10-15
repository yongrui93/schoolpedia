from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django import forms
from sso.models import User
import pdb


class UserCreationForm(DjangoUserCreationForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'email': 'Email Address',
        }

    def clean(self):
        self.cleaned_data = super(UserCreationForm, self).clean()
        username = self.cleaned_data.get('email')
        if not username or User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                'Email already registered. Please use another email',
                code='unique',
            )
        self.cleaned_data['username'] = username
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None
