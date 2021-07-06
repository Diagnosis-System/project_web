from django.contrib import admin
# from django.db import models
from .models import Symptom
from desease.models import Desease
# Register your models here.
class InlineDesease(admin.TabularInline):
    model = Desease
    extra = 2

@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    model = Symptom
    inlines = (InlineDesease, )
    list_display = ("id", "symptom_name")
    list_display_links = ("id", "symptom_name")
    list_filter = ("symptom_name",)
    search_fields = ("symptom_name",)
    ordering = ("-id",)