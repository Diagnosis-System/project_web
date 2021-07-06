from django.contrib import admin
from .models import Case, CaseSymptoms
from desease.models import Desease
import operator

@admin.register(CaseSymptoms)
class CaseSymptomAdmin(admin.ModelAdmin):
    pass


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
        # we only have the case units
        # we extract its symptoms objects
        sympotoms = []
        for unit_case in unit_cases:
            sympotoms.append(unit_case.symptom_name)
        
        # then we can get the deseases connected to the same symp
        # also create dict to have the count of the desease ocourence
        desease = {}
        for symptom in sympotoms:
            ds = Desease.objects.filter(symptom_name=symptom)
            for d in ds:
                try:
                    desease[str(d.desease_name)] += 1
                except:
                    desease[str(d.desease_name)] = 1
        
        sorted_d = dict(sorted(desease.items(), key=operator.itemgetter(1), reverse=True))
        
        max = 0
        i = 0
        for v in sorted_d.values():
            if v >= max:
                max = v
                i += 1
                continue
            break
        most_freq_desease = ' or '.join(list(sorted_d)[0:i])
        # if len(most_freq_desease) > 1:
        #     most_freq_desease = most_freq_desease
        # breakpoint()
        # desease_obj = Desease.objects.get(desease_name=most_freq_desease)

        return most_freq_desease

    # def save_model(self, request, obj, form, change):
    #     obj.desease_name = self.get_desease(list(CaseSymptoms.objects.filter(case=obj)))
    #     super().save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        obj.desease_name = self.get_desease(list(CaseSymptoms.objects.filter(case=obj)))
        return super().response_add(request, obj, post_url_continue=post_url_continue)
