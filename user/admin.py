from django.contrib import admin

from .models import Patient, Doctor

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
admin.site.register(Doctor)
admin.site.register(Patient)
