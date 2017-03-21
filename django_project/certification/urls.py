# coding=utf-8
"""urls for certification application"""

from django.conf.urls import patterns, url, include
from django.conf import settings
from views import (
    # Certifying Organisation
    CertifyingOrganisationCreateView,
    CertifyingOrganisationDeleteView,
    CertifyingOrganisationDetailView,
    CertifyingOrganisationListView,
    CertifyingOrganisationUpdateView,
    PendingCertifyingOrganisationListView,
    ApproveCertifyingOrganisationView,
    JSONCertifyingOrganisationListView,

    # Training Center
    TrainingCenterCreateView,
    TrainingCenterDeleteView,
    TrainingCenterDetailView,
    TrainingCenterListView,
    TrainingCenterUpdateView,
    JSONTrainingCenterListView
)

urlpatters = patterns(
    '',
    # Certifying Organisation management

# This view is only accessible via ajax
    url(regex='^json-certifyingorganisation/list/(?P<version>\d+)/$',
        view=JSONCertifyingOrganisationListView.as_view(),
        name='json-certifyingorganisation-list'),
    url(regex='^(?P<project_slug>[\w-]+)/pending-certifyingorganisation/list/$',
        view=PendingCertifyingOrganisationListView.as_view(),
        name='pending-certifyingorganisation-list'),
    url(regex='^(?P<project_slug>[\w-]+)/approve-certifyingorganisation/(?P<slug>[\w-]+)/$',
        view=ApproveCertifyingOrganisationView.as_view(),
        name='certifyingorganisation-approve'),
    url(regex='^(?P<project_slug>[\w-]+)/certifyingorganisations/list/$',
        view=CertifyingOrganisationListView.as_view(),
        name='certifyingorganisation-list'),
    url(regex='^(?P<project_slug>[\w-]+)/certifyingorganisation/(?P<slug>[\w-]+)/$',
        view=CertifyingOrganisationDetailView.as_view(),
        name='certifyingorganisation-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/certifyingorganisation/(?P<slug>[\w-]+)/delete/$',
        view=CertifyingOrganisationDeleteView.as_view(),
        name='certifyingorganisation-delete'),
    url(regex='^(?P<project_slug>[\w-]+)/create-certifyingorganisation/$',
        view=CertifyingOrganisationCreateView.as_view(),
        name='certifyingorganisation-create'),
    url(regex='^(?P<project_slug>[\w-]+)/certifyingorganisation/(?P<slug>[\w-]+)/update/$',
        view=CertifyingOrganisationUpdateView.as_view(),
        name='certifyingorganisation-update'),

    # Training Center management
    url(regex='^json-trainingcenter/list/(?P<version>\d+)/$',
        view=JSONTrainingCenterListView.as_view(),
        name='json-trainingcenter-list'),
    url(regex='^(?P<project_slug>[\w-]+)/trainingcenter/list/$',
        view=TrainingCenterListView.as_view(),
        name='trainingcenter-list'),
    url(regex='^(?P<project_slug>[\w-]+)/trainingcenter/(?P<slug>[\w-]+)/$',
        view=TrainingCenterDetailView.as_view(),
        name='trainingcenter-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/trainingcenter/(?P<slug>[\w-]+)/delete/$',
        view=TrainingCenterDeleteView.as_view(),
        name='trainingcenter-delete'),
    url(regex='^(?P<project_slug>[\w-]+)/create-trainingcenter/$',
        view=TrainingCenterCreateView.as_view(),
        name='trainingcenter-create'),
    url(regex='^(?P<project_slug>[\w-]+)/trainingcenter/(?P<slug>[\w-]+)/update/$',
        view=TrainingCenterUpdateView.as_view(),
        name='trainingcenter-update'),
)
