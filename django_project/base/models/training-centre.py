# coding=utf-8
"""Project model used by all apps."""

# import os
import logging
# import string
# import re
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# from django.conf.global_settings import MEDIA_ROOT
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.settings.contrib import STOP_WORDS
# from django.conf import settings
# from django.core.exceptions import ValidationError
from unidecode import unidecode


logger = logging.getLogger(__name__)

class ApprovedTCManager(models.Manager):
    """ Custom convener manager that shows only approved conveners """

    def get_queryset(self):
        """ Query set generator """
        return super(
            ApprovedTCManager, self).get_queryset().filter(approved=True)


class UnapprovedTCManager(models.Manager):
    """ Custom convener manager that shows only unapproved training centre """

    def get_queryset(self):
        """ Query set generator """
        return super(
            UnapprovedTCManager, self).get_queryset().filter(approved=False)


class TrainingCentre(models.Model):
    """ Training Centre / Organisation registration """
    name = models.CharField(
        help_text=_('Organisation/Institution name who intend to be a Training Centre'),
        max_length=150,
        null=False,
        blank=False,
        unique=True
    )

    email = models.CharField(
        help_text=_('Valid email address for communication purpose'),
        max_length=150,
        null=False,
        blank=False
    )

    Address = models.CharField(
        help_text=_('Address of the organisation/institution'),
        max_length=250,
        null=False,
        blank=False,
    )

    phone = models.CharField(
        help_text=_('Phone number/Landline'),
        max_length=150,
        null=False,
        blank=False
    )

    course = models.CharField(
        help_text=_('Course options'),
        max_length=250,
        null=False,
        blank=False
    )

    slug = models.SlugField(unique=True)
    objects = models.Manager()
    approved_objects = ApprovedTCManager()
    unapproved_objects = UnapprovedTCManager()

    # noinspection PyClassicStyleClass
    class Meta:
        """ Meta class for conveners """
        app_label = 'base'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """ Overloaded save method

        :param args:
        :param kwargs:
        """
        if not self.pk:
            words = self.name.split()
            filtered_words = [t for t in words if t.lower() not in STOP_WORDS]
            # unidecode() represents special characters (unicode data) in ASCII
            new_list = unidecode(' '.join(filtered_words))
            self.slug = slugify(new_list)[:50]

        super(TrainingCentre, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        """Return URL to convener detail page

        :return: URL
        :rtype: str

        """
        return reverse('convener-detail', kwargs={'slug': self.slug})
