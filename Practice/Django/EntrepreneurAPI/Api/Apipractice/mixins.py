from rest_framework import permissions
from rest_framework import authentication

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication]