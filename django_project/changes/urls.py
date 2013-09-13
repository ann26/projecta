# coding=utf-8
"""Urls for changelog application."""
from django.conf.urls import patterns, url
from django.conf import settings

from views import (
    # Project
    ProjectDetailView,
    ProjectDeleteView,
    ProjectCreateView,
    ProjectListView,
    ProjectUpdateView,
    PendingProjectListView,
    ApproveProjectView,
    # Category
    CategoryDetailView,
    CategoryDeleteView,
    CategoryCreateView,
    CategoryListView,
    JSONCategoryListView,
    CategoryUpdateView,
    PendingCategoryListView,
    ApproveCategoryView,
    # Version
    VersionMarkdownView,
    VersionDetailView,
    VersionThumbnailView,
    VersionDeleteView,
    VersionCreateView,
    VersionListView,
    VersionUpdateView,
    PendingVersionListView,
    ApproveVersionView,
    VersionDownload,
    # Entry
    EntryDetailView,
    EntryDeleteView,
    EntryCreateView,
    EntryListView,
    EntryUpdateView,
    PendingEntryListView,
    ApproveEntryView)

urlpatterns = patterns(
    '',
    # basic app views
    url(regex='^$',
        view=ProjectListView.as_view(),
        name='home'),
    # Project management
    url(regex='^pending-project/list/$',
        view=PendingProjectListView.as_view(),
        name='pending-project-list'),
    url(regex='^approve-project/(?P<pk>\d+)/$',
        view=ApproveProjectView.as_view(),
        name='project-approve'),
    url(regex='^project/list/$',
        view=ProjectListView.as_view(),
        name='project-list'),
    url(regex='^project/(?P<pk>\d+)/$',
        view=ProjectDetailView.as_view(),
        name='project-detail'),
    url(regex='^project/delete/(?P<pk>\d+)/$',
        view=ProjectDeleteView.as_view(),
        name='project-delete'),
    url(regex='^project/create/$',
        view=ProjectCreateView.as_view(),
        name='project-create'),
    url(regex='^project/update/(?P<pk>\d+)/$',
        view=ProjectUpdateView.as_view(),
        name='project-update'),

    # Category management

    # This view is only accessible via ajax
    url(regex='^json-category/list/(?P<version>\d+)/$',
        view=JSONCategoryListView.as_view(),
        name='json-category-list'),
    url(regex='^pending-category/list/$',
        view=PendingCategoryListView.as_view(),
        name='pending-category-list'),
    url(regex='^approve-category/(?P<pk>\d+)/$',
        view=ApproveCategoryView.as_view(),
        name='category-approve'),
    url(regex='^category/list/$',
        view=CategoryListView.as_view(),
        name='category-list'),
    url(regex='^category/(?P<pk>\d+)/$',
        view=CategoryDetailView.as_view(),
        name='category-detail'),
    url(regex='^category/delete/(?P<pk>\d+)/$',
        view=CategoryDeleteView.as_view(),
        name='category-delete'),
    url(regex='^category/create/$',
        view=CategoryCreateView.as_view(),
        name='category-create'),
    url(regex='^category/update/(?P<pk>\d+)/$',
        view=CategoryUpdateView.as_view(),
        name='category-update'),

    # Version management
    url(regex='^pending-version/list/$',
        view=PendingVersionListView.as_view(),
        name='pending-version-list'),
    url(regex='^approve-version/(?P<pk>\d+)/$',
        view=ApproveVersionView.as_view(),
        name='version-approve'),
    url(regex='^version/list/$',
        view=VersionListView.as_view(),
        name='version-list'),
    url(regex='^version-markdown/(?P<pk>\d+)/$',
        view=VersionMarkdownView.as_view(),
        name='version-markdown'),
    url(regex='^version/(?P<pk>\d+)/$',
        view=VersionDetailView.as_view(),
        name='version-detail'),
    url(regex='^version/thumbs/(?P<pk>\d+)/$',
        view=VersionThumbnailView.as_view(),
        name='version-thumbs'),
    url(regex='^version/delete/(?P<pk>\d+)/$',
        view=VersionDeleteView.as_view(),
        name='version-delete'),
    url(regex='^version/create/$',
        view=VersionCreateView.as_view(),
        name='version-create'),
    url(regex='^version/update/(?P<pk>\d+)/$',
        view=VersionUpdateView.as_view(),
        name='version-update'),
    url(regex='^version/download/(?P<pk>\d+)/$',
        view=VersionDownload.as_view(),
        name='version-download'),

    # Changelog entry management
    url(regex='^pending-entry/list/$',
        view=PendingEntryListView.as_view(),
        name='pending-entry-list'),
    url(regex='^approve-entry/(?P<pk>\d+)/$',
        view=ApproveEntryView.as_view(),
        name='entry-approve'),
    url(regex='^entry/list/$',
        view=EntryListView.as_view(),
        name='entry-list'),
    url(regex='^entry/(?P<pk>\d+)/$',
        view=EntryDetailView.as_view(),
        name='entry-detail'),
    url(regex='^entry/delete/(?P<pk>\d+)/$',
        view=EntryDeleteView.as_view(),
        name='entry-delete'),
    url(regex='^entry/create/$',
        view=EntryCreateView.as_view(),
        name='entry-create'),
    url(regex='^entry/update/(?P<pk>\d+)/$',
        view=EntryUpdateView.as_view(),
        name='entry-update'),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
