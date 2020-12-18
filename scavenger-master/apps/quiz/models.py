from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Question(models.Model):
    question = models.TextField(_('Question'))
    answer = models.CharField(_('Answer'), max_length=200)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option')
    choice = models.CharField(_("Choice"), max_length=200)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'


class Winner(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=100)
    image = models.FileField(_('Winner Image'), upload_to='winners/', null=True, blank=True)

    class Meta:
        verbose_name = 'Winner'
        verbose_name_plural = 'Winners'

    def __str__(self):
        return str(self.name)
