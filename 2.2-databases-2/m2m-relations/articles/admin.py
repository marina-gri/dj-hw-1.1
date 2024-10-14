from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        tags = set()
        is_main_count = 0
        form_count = 0
        list_error = []
        for form in self.forms:
            if form.cleaned_data['DELETE']:
                continue
            form_count += 1
            tags.add(form.cleaned_data.get('tag'))
            if form.cleaned_data.get('is_main') is True:
                is_main_count += 1
        if form_count != len(tags):
            list_error.append('Есть дубликаты тем.')

        if is_main_count < 1:
            list_error.append('Необходимо выбрать главную тему.')
        elif is_main_count > 1:
            list_error.append('Выберите только одну главную тему.')

        if len(list_error):
            raise ValidationError(' '.join(list_error))
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
