from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.models import Group

# ====================================================
# # Register your models here.
# admin.site.register(User)

# ====================================================
# # Or Register your models here with default UserAdmin.


# class CustomUserAdmin(UserAdmin):
#     list_display = ["username", "email", "first_name", "last_name"]


# admin.site.register(User, CustomUserAdmin)

# ====================================================
# # Or Register your models here with custom UserAdmin.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]


# ====================================================
# Un-Register your models here
admin.site.unregister(Group)
