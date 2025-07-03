from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    search_fields = ('model',)
    list_filter = ('manufacturer',)
    filter_horizontal = ('drivers',)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'license_number')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Additional info', {'fields': ('license_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'license_number'),
        }),
    )
