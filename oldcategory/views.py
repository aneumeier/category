#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
"""

from django.views.generic import CreateView, UpdateView
from django.views.generic import DetailView, ListView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from models import Category, Tag
from forms import CategoryCreateForm, TagCreateForm, CategoryUpdateForm

class CategoryListView(ListView):
    """
    List all registered feeds

    """
    model = Category
    context_object_name = "categories"
    paginate_by = 10

class CategoryDetailView(DetailView):
    """
    Show details for a particular Category

    ToDo:
    this shall include stats
    """
    model = Category

    def dispatch(self, *args, **kwargs):
        return super(CategoryDetailView, self).dispatch(*args, **kwargs)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update a particular Category
    """
    form_class = CategoryUpdateForm
    model = Category

    def get_success_url(self):
        if 'slug' in self.kwargs:
            return reverse('planet:category-view', self.kwargs['slug'])
        else:
            return reverse('planet:category-home')

class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
    ToDo:
    make this more nice & userfriendly
    """
    form_class = CategoryCreateForm
    model = Category
    initial = {'is_Active': False}

class TagListView(ListView):
    """
    List all registered tags

    """
    model = Tag
    context_object_name = "tags"
    paginate_by = 10
    queryset = Tag.objects.all()

class TagDetailView(DetailView):
    """
    Show details for a particular tag.

    ToDo:
    this shall include stats
    """
    model = Tag
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super(TagDetailView, self).dispatch(*args, **kwargs)

class TagCreateView(LoginRequiredMixin, CreateView):
    """
    ToDo:
    make this more nice & userfriendly
    """
    form_class = TagCreateForm
    model = Tag
    initial = {'is_Active': False}

class TagUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Update particular tag
    """
    permission_required = "feeds.update_tag"
    model = Tag


