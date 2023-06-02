from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# local imports
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets = (
        (None, {
            'fields': (
                "name",
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': (
                "name",
            ),
        }),
    )


admin.register(CustomUser, CustomUserAdmin)
