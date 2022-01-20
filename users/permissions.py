from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_student

class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_agent
        
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin
