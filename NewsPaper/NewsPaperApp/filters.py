# -*- coding: utf-8 -*-
from django_filters import FilterSet
from .models import Post
from django.forms import DateInput

import django_filters


class PostFilter(FilterSet):

    author = django_filters.CharFilter(field_name='author_id__user_id__username', lookup_expr='icontains', label='Автор')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок')
    datetime = django_filters.DateFilter(field_name='date', widget=DateInput(attrs={'type': 'date'}), lookup_expr='gt', label='Позже даты')

    class Meta:
        model = Post
        fields = []
