#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns, include

from category.views import CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView
from category.views import TagListView, TagDetailView, TagCreateView, TagUpdateView


urlpatterns = patterns('',
    url(r'^category/$', CategoryListView.as_view(), name="category-home"),
    url(r'^category/page/(?P<page>\w+)/$', CategoryListView.as_view(), name="category-home-paginated"),
    url(r'^category/add/$', CategoryCreateView.as_view(), name="category-add"),
    url(r'^category/(?P<slug>\w+)/$', CategoryDetailView.as_view(), name="category-view"),
    url(r'^category/(?P<slug>\w+)/update$', CategoryUpdateView.as_view(), name="category-update"),
)

urlpatterns += patterns('',
    url(r'^tag /$', TagListView.as_view(), name="tag-home"),
    url(r'^tag/page/(?P<page>\w+)/$', TagListView.as_view(), name="tag-home-paginated"),
    url(r'^tag/add/$', TagCreateView.as_view(), name="tag-add"),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagDetailView.as_view(), name="tag-view"),
    url(r'^tag/(?P<id>\d+)/update/$', TagUpdateView.as_view(), name="tag-update"),
)

