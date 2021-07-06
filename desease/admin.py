from django.contrib import admin
from .models import Desease

@admin.register(Desease)
class DeseaseAdmin(admin.ModelAdmin):
    model = Desease
    list_display = ("id", "desease_name", "symptom_name")
    list_display_links = ("id", "desease_name")
    list_filter = ("desease_name",)
    search_fields = ("desease_name",)
    ordering = ("-id",)
