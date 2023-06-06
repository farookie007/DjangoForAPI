from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        'username',
        'email',
        'name',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': (
                'name',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'name',
            ),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
