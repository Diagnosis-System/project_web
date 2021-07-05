from django.contrib import admin
# from django.db import models
from .models import Symptom
# Register your models here.
@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    model = Symptom
    list_display = ("id", "symptom_name", "desease_name")
    list_display_links = ("id", "symptom_name")
    list_filter = ("symptom_name",)
    search_fields = ("symptom_name",)
    ordering = ("-id",)