from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):

    # Champs personnalisés

    role_field = 'role'