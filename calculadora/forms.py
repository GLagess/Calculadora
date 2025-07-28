from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    username = forms.CharField(label="Nome de usuário", max_length=150)
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirmação da senha",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Já existe um usuário com esse nome.")
        return username

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("As senhas não conferem.")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
