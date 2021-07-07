from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Symptom 
from .forms import SymptomForm
from case.models import Case
# Create your views here.

def Symname(request):
   # case = get_object_or_404 (Case,symptom_name)
   
    new_symptom = None

    if request.method == 'POST' :
        
        
        #symptom was posted
        symptom_form = SymptomForm(data=request.POST)
        if symptom_form.is_valid() :
            #create symptom object but dont save to database
            new_symptom = symptom_form.save(commit = False)
            #Assign the current case to the symptom
            #new_symptom.case = case
            #Save the symptom to the database
            new_symptom.save()
    else :
        symptom_form = SymptomForm()
    
    return render(request,
                  'patient_symptoms.html',
                  {#'case':case,
                #    'symptoms':symptoms ,
                   'new_symptom': new_symptom ,
                   'symptom_form' : symptom_form})