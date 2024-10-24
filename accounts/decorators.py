from django.core.exceptions import PermissionDenied
from functools import wraps

def role_required(allowed_roles=None):
    """
    Decorator to check if a user has the appropriate role to access a view.
    
    :param allowed_roles: A list of roles that are allowed to access the view.
    """
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user

            # Check if the user is authenticated
            if not user.is_authenticated:
                raise PermissionDenied  # Not logged in, deny access

            # Check for specific roles based on inheritance
            if hasattr(user, 'admin') and 'admin' in allowed_roles:
                return view_func(request, *args, **kwargs)
            elif hasattr(user, 'staff') and 'staff' in allowed_roles:
                return view_func(request, *args, **kwargs)
            elif hasattr(user, 'librarian') and 'librarian' in allowed_roles:
                return view_func(request, *args, **kwargs)

            # If user doesn't have the required role, deny access
            raise PermissionDenied

        return _wrapped_view

    return decorator
