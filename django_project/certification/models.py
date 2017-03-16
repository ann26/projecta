# coding=utf-8
"""
Model definitions for certification apps
"""

import os
import logging
import string
import re
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.conf.global_settings import MEDIA_ROOT
from django.utils.translation import ugettext_lazy as _
from core.settings.contrib import STOP_WORDS
from django.conf import settings
from django.core.exceptions import ValidationError
from unidecode import unidecode


logger = logging.getLogger(__name__)
app_label = 'certification'


class SlugModel(object):
    
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            words = self.name.split()
            filtered_words = [t for t in words if t.lower() not in STOP_WORDS]
            # unidecode() represents special characters (unicode data) in ASCII
            new_list = unidecode(' '.join(filtered_words))
            self.slug = slugify(new_list)[:50]

        super(SlugModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class CourseType(SlugModel, models.Model):
    """Course Type model."""

    name = models.CharField(
        help_text="Course type.",
        max_length=200,
        null=False,
        blank=False
    )

    slug = models.SlugField(unique=True)
    objects = models.Manager()
    course = models.ManyToManyField(Course)

    # noinspection PyClassicStyleClass.
    class Meta:
        """Meta class for Course types."""

        ordering = ['name']

    def save(self, *args, **kwargs):
        super(CourseType, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        """Return URL to course type detail page.
        :return: URL
        :rtype: str
        """
        return reverse('course-type-detail', kwargs={'slug': self.slug})


class TrainingCenter(SlugModel, models.Model):
    """Training Centre / Organisation registration."""

    name = models.CharField(
        help_text=_('Organisation/Institution name.'),
        max_length=150,
        null=False,
        blank=False,
        unique=True
    )

    email = models.CharField(
        help_text=_('Valid email address for communication purpose.'),
        max_length=150,
        null=False,
        blank=False
    )

    Address = models.CharField(
        help_text=_('Address of the organisation/institution.'),
        max_length=250,
        null=False,
        blank=False,
    )

    phone = models.CharField(
        help_text=_('Phone number/Landline.'),
        max_length=150,
        null=False,
        blank=False
    )

    slug = models.SlugField(unique=True)
    objects = models.Manager()
    course = models.ManyToManyField(Course)

    # noinspection PyClassicStyleClass.
    class Meta:
        """Meta class for training centre."""

        ordering = ['name']

    def save(self, *args, **kwargs):
        super(TrainingCenter, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        """Return URL to training center detail page.
        :return: URL
        :rtype: str
        """
        return reverse('training-center-detail', kwargs={'slug': self.slug})


class Attendee(SlugModel, models.Model):
    """Course Attendee model."""

    firstname = models.CharField(
        help_text="First name course attendee.",
        max_length=200,
        null=False,
        blank=False
    )

    surname = models.CharField(
        help_text="Surname course attendee.",
        max_length=200,
        null=False,
        blank=False
    )

    email = models.CharField(
        help_text="Email address.",
        max_length=200,
        null=False,
        blank=False
    )

    slug = models.SlugField(unique=True)
    objects = models.Manager()
    certificate = models.ForeignKey(Certificate, models.CASCADE)

    # noinspection PyClassicStyleClass.
    class Meta:
        """ Meta class for Course attendee."""

        ordering = ['firstname']

    def save(self, *args, **kwargs):
        super(Attendee, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        """Return URL to attendee detail page.
        :return: URL
        :rtype: str
        """
        return reverse('attendee-detail', kwargs={'slug': self.slug})


class Certificate(models.Model):
    """Certificate model."""

    def get_absolute_url(self):
        """Return URL to certificate detail page.
        :return: URL
        :rtype: str
        """
        return reverse('certificate-detail', kwargs={'slug': self.slug})


class Course(SlugModel, models.Model):
    """Course model."""

    name = models.CharField(
        help_text="Course name.",
        max_length=200,
        null=False,
        blank=False,
    )

    def save(self, *args, **kwargs):
        super(Course, self).save(self, *args, **kwargs)

    slug = models.SlugField(unique=True)
    objects = models.Manager()
    course_attendee = models.ManyToManyField(Attendee)
    certificate = models.ForeignKey(Certificate, models.CASCADE)

    def __unicode__(self):
        return u'%s' %self.name

    def get_absolute_url(self):
        """Return URL to course detail page.
        :return: URL
        :rtype: str
        """
        return reverse('course-detail', kwargs={'slug': self.slug})


class CourseConvener(SlugModel, models.Model):
    """Course Convener model."""

    slug = models.SlugField(unique=True)
    objects = models.Manager()
    course = models.ManyToManyField(Course)

    def save(self, *args, **kwargs):
        super(CourseConvener, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        """Return URL to course convener detail page.
        :return: URL
        :rtype: str
        """
        return reverse('course-convener-detail', kwargs={'slug': self.slug})


class ApprovedCertifyingOrganisationManager(models.Manager):
    """Custom training centre manager, shows only approved training center."""

    def get_queryset(self):
        """ Query set generator. """

        return super(
            ApprovedCertifyingOrganisationManager, self).get_queryset().filter(
                approved=True)


class UnapprovedCertifyingOrganisationManager(models.Manager):
    """Custom training centre manager, shows only unapproved training centre."""

    def get_queryset(self):
        """ Query set generator. """

        return super(
            UnapprovedCertifyingOrganisationManager, self).get_queryset(
        ).filter(approved=False)


class CertifyingOrganisation(SlugModel, models.Model):
    """ Certifying organisation model."""

    organisation_name = models.CharField(
        help_text="Name of Organisation or Institution.",
        max_length=200,
        null=False,
        blank=False
    )

    organisation_email = models.CharField(
        help_text="Email address Organisation or Institution.",
        max_length=200,
        null=False,
        blank=False
    )

    organisation_phone = models.CharField(
        help_text="Contact of Organisation or Institution.",
        max_length=200,
        null=False,
        blank=False
    )

    approved = models.BooleanField(
        help_text="Approval from project admin",
        default=False
    )

    slug = models.SlugField(unique=True)

    course_type = models.ManyToManyField(CourseType)
    course = models.ManyToManyField(Course)
    training_center = models.ManyToManyField(TrainingCenter)
    course_convener = models.ManyToManyField(CourseConvener)
    project = models.ForeignKey('base.Project')
    objects = models.Manager()
    approved_objects = ApprovedCertifyingOrganisationManager()
    unapproved_objects = UnapprovedCertifyingOrganisationManager()

    # noinspection PyClassicStyleClass.
    class Meta:
        """ Meta class for Course attendee."""

        ordering = ['organisation_name']

    def save(self, *args, **kwargs):
        super(CertifyingOrganisation, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        """Return URL to certifying organisation detail page.
        :return: URL
        :rtype: str
        """
        return reverse(
            'certifying-organisation-detail', kwargs={'slug': self.slug})

