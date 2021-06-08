# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Post, Category


class CreatePostForm(ModelForm):

    type = forms.ChoiceField(
        choices=Post.POSITIONS,
        label='Тип',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    title = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
    )

    categories = forms.ModelMultipleChoiceField(
        label='Категория',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input create-post-categories'}),
        queryset=Category.objects.all(),
    )

    text = forms.CharField(
        label='Текст',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
    )

    mailing = forms.CharField(
        label='Рассылка по e-mail',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'checked': 'True', 'id': 'mailing'}),
        required=False
    )

    class Meta:
        model = Post
        fields = ['type', 'title', 'categories', 'text', 'mailing']

