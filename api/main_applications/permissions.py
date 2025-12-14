from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        user = request.user

        if request.method == "DELETE":
            return user.is_staff or obj.owner == user

        if request.method in ["PUT", "PATCH"]:
            return obj.owner == user

        return False


















# from rest_framework.permissions import BasePermission, SAFE_METHODS

# class PostPermission(BasePermission):

#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
        
#         user = request.user

#         if user.is_staff:
#             return True
#         return obj.user == user
