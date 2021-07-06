from django.contrib import admin
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django import forms
from django.urls import path
from django.shortcuts import get_object_or_404
import csv
import codecs

from .models import Desease
from symptoms.models import Symptom

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(Desease)
class DeseaseAdmin(admin.ModelAdmin):
    model = Desease
    list_display = ("id", "desease_name", "symptom_name")
    list_display_links = ("id", "desease_name")
    list_filter = ("desease_name",)
    search_fields = ("desease_name",)
    ordering = ("-id",)

    change_list_template = "admin/product_change_list.html"

    def get_urls(self):
            urls = super().get_urls()
            my_urls = [
                path("admin/import-csv/", self.import_csv),
            ]
            return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            imported_file = request.FILES["csv_file"]
            csv_file = csv.DictReader(codecs.iterdecode(imported_file, "utf-8"))
            column_names = []
            for name in csv_file.fieldnames:
                if name == 'المرض':
                    continue
                try:
                    Symptom.objects.get(symptom_name=name)
                    column_names.append(name)
                    continue
                except:
                    Symptom.objects.create(symptom_name=name)
                    column_names.append(name)
            for line in csv_file:
                des_name = line['المرض']
                for name in column_names:
                    if name == 'المرض':
                        continue
                    if line[name] == 'Y':
                        symp = get_object_or_404(Symptom, symptom_name=name)
                        try:
                            breakpoint()
                            Desease.objects.get(desease_name=des_name, symptom_name=symp)
                            continue
                        except:
                            Desease.objects.create(desease_name=des_name, symptom_name=symp)
            self.message_user(request, "Your csv file has been imported")
            return redirect(reverse("admin:desease_desease_changelist"))
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)
