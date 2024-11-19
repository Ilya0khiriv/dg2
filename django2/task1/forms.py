from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Введите логин:')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Введите пароль:')
    password_2 = forms.CharField(widget=forms.PasswordInput, required=True, label='Повторите пароль:')
    age = forms.CharField(max_length=3, required=True, label='Введите свой возраст:')
