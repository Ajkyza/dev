from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    # Champs personnalisés

    role = forms.ChoiceField(
        label='Rôle',
        choices=[('Moi seul', 'Moi seul'), ('Principal', 'Principal'), ('SG', 'SG'), ('Agent', 'Agent')],
        widget=forms.RadioSelect,
    )