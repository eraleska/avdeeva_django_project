from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Такой пользователь не существует')
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
            if not user.is_active:
                raise forms.ValidationError('Этот аккаунт неактивен')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Адрес электронной почты')
    email2 = forms.EmailField(label='Подтвердите адрес')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Адреса электронных почт должны совпадать")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Такой адрес уже существует")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
