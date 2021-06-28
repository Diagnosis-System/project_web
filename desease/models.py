from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Desease(models.Model):
    class Meta:
        verbose_name = _("desease")
        verbose_name_plural = _("deseases")

    # required
    desease_name = models.CharField(max_length=255, blank=True)

