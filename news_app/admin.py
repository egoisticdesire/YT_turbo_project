from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from news_app.models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    save_on_top = True
    list_display = (
        'id',
        'title',
        'category',
        'created_at',
        'updated_at',
        'photo',
        'views',
        'is_published',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'is_published',
        'category',
    )
    fields = (
        'title',
        'category',
        'content',
        'photo',
        'get_photo',
        'is_published',
        'views',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'title',
        'content',
    )
    readonly_fields = (
        'get_photo',
        'views',
        'created_at',
        'updated_at',
    )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=300px>')

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_display_links = (
        'id',
        'title',
    )
    search_fields = (
        'title',
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
