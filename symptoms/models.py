from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Symptom(models.Model):
    class Meta:
        verbose_name = _("symptom")
        verbose_name_plural = _("symptoms")

    # required
    symptom_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.symptom_name
