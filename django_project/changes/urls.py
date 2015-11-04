# coding=utf-8
"""Urls for changelog application."""

from django.conf.urls import patterns, url, include  # noqa

from django.conf import settings

from feeds.version import RssVersionFeed, AtomVersionFeed
from feeds.entry import RssEntryFeed, AtomEntryFeed
from views import (
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
    ApproveEntryView,
    # Sponsor
    SponsorDetailView,
    SponsorDeleteView,
    SponsorCreateView,
    SponsorListView,
    JSONSponsorListView,
    SponsorUpdateView,
    PendingSponsorListView,
    ApproveSponsorView
)

urlpatterns = patterns(
    '',
    # Category management

    # This view is only accessible via ajax
    url(regex='^json-category/list/(?P<version>\d+)/$',
        view=JSONCategoryListView.as_view(),
        name='json-category-list'),
    url(regex='^(?P<project_slug>[\w-]+)/pending-category/list/$',
        view=PendingCategoryListView.as_view(),
        name='pending-category-list'),
    url(regex='^(?P<project_slug>[\w-]+)/approve-category/(?P<slug>[\w-]+)/$',
        view=ApproveCategoryView.as_view(),
        name='category-approve'),
    url(regex='^(?P<project_slug>[\w-]+)/category/list/$',
        view=CategoryListView.as_view(),
        name='category-list'),
    url(regex='^(?P<project_slug>[\w-]+)/category/(?P<slug>[\w-]+)/$',
        view=CategoryDetailView.as_view(),
        name='category-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/category/(?P<slug>[\w-]+)/delete/$',
        view=CategoryDeleteView.as_view(),
        name='category-delete'),
    url(regex='^(?P<project_slug>[\w-]+)/create-category/$',
        view=CategoryCreateView.as_view(),
        name='category-create'),
    url(regex='^(?P<project_slug>[\w-]+)/category/(?P<slug>[\w-]+)/update/$',
        view=CategoryUpdateView.as_view(),
        name='category-update'),

    # Version management
    url(regex='^(?P<project_slug>[\w-]+)/pending-versions/list/$',
        view=PendingVersionListView.as_view(),
        name='pending-version-list'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<slug>[\w.-]+)/approve/$',
        view=ApproveVersionView.as_view(),
        name='version-approve'),
    url(regex='^(?P<project_slug>[\w-]+)/version/list/$',
        view=VersionListView.as_view(),
        name='version-list'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<slug>[\w.-]+)/markdown/$',
        view=VersionMarkdownView.as_view(),
        name='version-markdown'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<slug>[\w.-]+)/$',
        view=VersionDetailView.as_view(),
        name='version-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<slug>[\w.-]+)/thumbs/$',
        view=VersionThumbnailView.as_view(),
        name='version-thumbs'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<slug>[\w.-]+)/delete/$',
        view=VersionDeleteView.as_view(),
        name='version-delete'),
    url(regex='^(?P<project_slug>[\w-]+)/create-version/$',
        view=VersionCreateView.as_view(),
        name='version-create'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<slug>[\w.-]+)/update/$',
        view=VersionUpdateView.as_view(),
        name='version-update'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<slug>[\w.-]+)/download/$',
        view=VersionDownload.as_view(),
        name='version-download'),

    # Changelog entry management
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w.-]+)/'
              'pending-entry/list/$',
        view=PendingEntryListView.as_view(),
        name='pending-entry-list'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w.-]+)/entry/'
              '(?P<slug>[\w-]+)/approve/$',
        view=ApproveEntryView.as_view(),
        name='entry-approve'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w'
              '.-]+)/entry/list/$',
        view=EntryListView.as_view(),
        name='entry-list'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w.-]+)/entry'
              '/(?P<slug>[\w-]+)/$',
        view=EntryDetailView.as_view(),
        name='entry-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w.-]+)/entry/'
              '(?P<slug>[\w-]+)/delete/$',
        view=EntryDeleteView.as_view(),
        name='entry-delete'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w.-]+)/'
              'create-entry/$',
        view=EntryCreateView.as_view(),
        name='entry-create'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w.-]+)/entry/'
              '(?P<slug>[\w-]+)/update/$',
        view=EntryUpdateView.as_view(),
        name='entry-update'),

    # Feeds
    url(regex='^(?P<project_slug>[\w-]+)/rss/latest-version/$',
        view=RssVersionFeed(),
        name='latest-version-rss-feed'),
    url(regex='^(?P<project_slug>[\w-]+)/atom/latest-version/$',
        view=AtomVersionFeed(),
        name='latest-version-atom-feed'),
    url(regex='^(?P<project_slug>[\w-]+)/rss/latest-entry/$',
        view=RssEntryFeed(),
        name='latest-entry-rss-feed'),
    url(regex='^(?P<project_slug>[\w-]+)/atom/latest-entry/$',
        view=AtomEntryFeed(),
        name='latest-entry-atom-feed'),

    # Feeds specific version and projects
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>['
              '\w.-]+)/rss$',
        view=RssEntryFeed(),
        name='entry-rss-feed'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>['
              '\w.-]+)/atom$',
        view=AtomEntryFeed(),
        name='entry-atom-feed'),

    # User map
    # url(r'^user-map/', include('user_map.urls')),

    # Sponsor management

    # This view is only accessible via ajax
    url(regex='^json-sponsor/list/(?P<version>\d+)/$',
        view=JSONSponsorListView.as_view(),
        name='json-sponsor-list'),
    url(regex='^(?P<project_slug>[\w-]+)/pending-sponsor/list/$',
        view=PendingSponsorListView.as_view(),
        name='pending-sponsor-list'),
    url(regex='^(?P<project_slug>[\w-]+)/approve-sponsor/(?P<slug>[\w-]+)/$',
        view=ApproveSponsorView.as_view(),
        name='sponsor-approve'),
    url(regex='^(?P<project_slug>[\w-]+)/sponsor/list/$',
        view=SponsorListView.as_view(),
        name='sponsor-list'),
    url(regex='^(?P<project_slug>[\w-]+)/sponsor/(?P<slug>[\w-]+)/$',
        view=SponsorDetailView.as_view(),
        name='sponsor-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/sponsor/(?P<slug>[\w-]+)/delete/$',
        view=SponsorDeleteView.as_view(),
        name='sponsor-delete'),
    url(regex='^(?P<project_slug>[\w-]+)/create-sponsor/$',
        view=SponsorCreateView.as_view(),
        name='sponsor-create'),
    url(regex='^(?P<project_slug>[\w-]+)/sponsor/(?P<slug>[\w-]+)/update/$',
        view=SponsorUpdateView.as_view(),
        name='sponsor-update'),

)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
