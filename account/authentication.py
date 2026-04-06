from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile


class EmailAndUsernameAuthBackend:
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        if not username or not password :
            return None

        users = User.objects.filter(Q(email__iexact=username) | Q(username=username))

        if users.count() > 1:
            return None
        
        user = users.first()

        if user and user.check_password(password):
            return user
        
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, response, *args, **kwargs):
    """
    Create user profile for social authentication
    """
    Profile.objects.get_or_create(user=user)