from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Local imports
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
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


admin.site.register(CustomUser, CustomUserAdmin)