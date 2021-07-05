from django.contrib import admin
from .models import Case, CaseSymptoms


class InlineCaseSymptoms(admin.TabularInline):
    model = CaseSymptoms
    extra = 2

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    model = Case
    inlines = (InlineCaseSymptoms, )
    list_display = ("id", "patient_name", "desease_name")
    list_display_links = ("id", "patient_name")
    list_filter = ("patient_name",)
    search_fields = ("patient_name",)
    ordering = ("-id",)

    def get_desease(self, unit_cases):
        '''
        get the input symptoms
        filter it and get the desease attached and count the desease
        get the most frequent one and put ut in desease_name field
        '''
        sympotoms = []
        for unit_case in unit_cases:
            sympotoms.append(unit_case.symptom_name)
        
        desease = {}
        for symptom in sympotoms:
            if desease[str(symptom.desease_name)]:
                desease[str(symptom.desease_name)] += 1
            else:
                desease[str(symptom.desease_name)] = 1

        pass

    def response_add(self, request, obj, post_url_continue=None):
        obj.desease_name = self.get_desease(list(CaseSymptoms.objects.filter(case=obj)))
        # if UserGroup.CASHIER in user.type:
        #     Invoice.objects.create(user=user, order=obj)
        return super().response_add(request, obj, post_url_continue=post_url_continue)
