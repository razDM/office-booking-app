from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import AuthUser
from selection.models import Floor,Office,Zone
from offices.models import Reservation


@admin.register(AuthUser)
class AdminAuthUser(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('name','floor_levels')


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name','floor','zone_location')


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name','zone')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user','office','start_date','end_date')