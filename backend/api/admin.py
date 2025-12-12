from django.contrib import admin
from .models import UserProfile, OTPVerification

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'created_at', 'updated_at']
    search_fields = ['user__username', 'user__email', 'phone']
    list_filter = ['created_at']


@admin.register(OTPVerification)
class OTPVerificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'otp', 'purpose', 'is_used', 'created_at', 'expires_at']
    search_fields = ['user__username', 'user__email', 'otp']
    list_filter = ['purpose', 'is_used', 'created_at']
    readonly_fields = ['created_at', 'expires_at']
