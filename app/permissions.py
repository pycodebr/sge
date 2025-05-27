from rest_framework import permissions

class CustomDjangoModelPermission(permissions.DjangoModelPermissions):
    # Override to improve the permissions on API
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],     
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
