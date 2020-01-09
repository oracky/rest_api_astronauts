from django.db import models
from django.utils.translation import gettext_lazy as _


class Astronaut(models.Model):
    id = models.PositiveIntegerField(verbose_name=_('ID'), null=False, blank=False, primary_key=True)
    name = models.CharField(verbose_name=_('First Name'), max_length=15)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=15)
    birth_date = models.DateField(verbose_name=_('Date of birth'), blank=True, default=None, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name = _('Astronaut')
        verbose_name_plural = _('Astronauts')