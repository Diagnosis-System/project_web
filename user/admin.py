from django.contrib import admin

from .models import Patient, Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ("id", "name", "mobile", "mail", "major")
    list_display_links = ("id", "name")
    list_filter = ("major",)
    search_fields = ("name",)
    ordering = ("-id",)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ("id", "name", "mobile", "mail", "age", "gender")
    list_display_links = ("id", "name")
    list_filter = ("gender",)
    search_fields = ("name",)
    ordering = ("-id",)
